# This is a Python Dictionary representing an M-Pesa payment request
mpesa_payload = {
    "BusinessShortCode": 174379,          # Key: String, Value: Integer
    "PhoneNumber": "254700111222",        # Key: String, Value: String
    "Amount": 500,                        # Key: String, Value: Integer
    "TransactionType": "CustomerPayBill", # Key: String, Value: String
    "IsTestEnvironment": True             # Key: String, Value: Boolean
}

# 1. Printing the entire filing cabinet (the whole dictionary)
print("--- FULL DICTIONARY ---")
print(mpesa_payload)
print("\n") # This just prints a blank line to make it look neat

# 2. Extracting just ONE specific value using its Key
# We use square brackets [] to ask the dictionary for a specific Key
print("--- EXTRACTING SPECIFIC VALUES ---")
print("The customer will be billed Ksh:")
print(mpesa_payload["Amount"])

print("The prompt will be sent to:")
print(mpesa_payload["PhoneNumber"])