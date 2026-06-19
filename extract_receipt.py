# This is an exact copy of a successful STK Push receipt from Safaricom.
# Notice how it has curly braces {} inside curly braces!
safaricom_receipt = {
    "Body": {
        "stkCallback": {
            "MerchantRequestID": "29115-34620561-1",
            "CheckoutRequestID": "ws_CO_19122023153020000",
            "ResultCode": 0,
            "ResultDesc": "The service request is processed successfully.",
            "CallbackMetadata": {
                "Item": [
                    {"Name": "Amount", "Value": 1.00},
                    {"Name": "MpesaReceiptNumber", "Value": "NLJ7RT61SV"},
                    {"Name": "Balance"},
                    {"Name": "TransactionDate", "Value": 20191219102115},
                    {"Name": "PhoneNumber", "Value": 254700000000}
                ]
            }
        }
    }
}

print("--- EXAMINING THE RECEIPT ---\n")

# Step 1: Let's check if the payment actually succeeded!
# We drill down: Body -> stkCallback -> ResultCode
result_code = safaricom_receipt["Body"]["stkCallback"]["ResultCode"]
result_desc = safaricom_receipt["Body"]["stkCallback"]["ResultDesc"]

if result_code == 0:
    print(f"✅ Payment Success! Safaricom says: {result_desc}")
    
    # Step 2: Since it succeeded, let's drill down to the Metadata items
    metadata_items = safaricom_receipt["Body"]["stkCallback"]["CallbackMetadata"]["Item"]
    
    # Step 3: Extract the specific values. 
    # Because 'Item' is a List (notice the square brackets [] in the dictionary),
    # we can grab the Amount (which is the 1st item, index 0) 
    # and the Receipt (which is the 2nd item, index 1)
    
    amount_paid = metadata_items[0]["Value"]
    receipt_number = metadata_items[1]["Value"]
    phone_number = metadata_items[4]["Value"]
    
    print("\n--- FINAL RECEIPT FOR VENDOR ---")
    print(f"Customer {phone_number} successfully paid Ksh {amount_paid}.")
    print(f"Official M-Pesa Code: {receipt_number}")
    print("Action: You can now release the goods to the customer!")

else:
    # If the ResultCode was 1032, it means the customer canceled or had no balance.
    print(f"❌ Payment Failed. Safaricom says: {result_desc}")
    print("Action: Do NOT release the goods")