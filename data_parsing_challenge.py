#This is a mock response from an API containing a list of today's transactions.
#Notice that "Transactions" contains a List [] of three different dictionaries {}!

daily_report = {
    "Date": "2023-10-27",
    "Vendor": "Tabitha's Shop",
    "Total_Customers": 3,
    "Transactions": [
        {"Receipt": "ABC123XYZ", "Amount": 500, "Status": "Success", "Phone": "254711111111"},
        {"Receipt": "DEF456UVW", "Amount": 1500, "Status": "Failed", "Phone": "254722222222"},
        {"Receipt": "GHI789RST", "Amount": 200, "Status": "Success", "Phone": "254733333333"}
    ]
}

print("--- DAILY SALES REPORT ---")
# Let's print the vendor name to start:
print(f"Store: {daily_report['Vendor']}\n")

# ==========================================
# YOUR CHALLENGE: Fill in the missing pieces!
# ==========================================

# CHALLENGE 1: Extract the Amount of the FIRST transaction (Should be 500)
# Hint: Drill down into "Transactions", grab the first item [0], then the "Amount"
first_amount = daily_report["Transactions"][0]["Amount"]
print(f"1. The first customer paid: Ksh {first_amount}")


# CHALLENGE 2: Extract the Phone Number of the SECOND transaction (Should be 254722222222)
second_phone_no = daily_report ["Transactions"][1]["Phone"]
print(f"2. The second customer's phone is: {second_phone_no}")


# CHALLENGE 3: Extract the Status of the THIRD transaction (Should be Success)
# Write your code here:
third_status = daily_report["Transactions"][2]["Status"]
print(f"3. The third transaction was a: {third_status}")


# BONUS BOSS LEVEL (Optional): 
# Can you write an 'if' statement that checks if the second transaction failed?
# If it failed, print("Do not deliver order 2!")
second_status = daily_report["Transactions"][1]["Status"]
if second_status == "Failed":
 print(f"Do not deliver order 2!")
 #expected indented block after if statement.Also note the '==' and ':'