# 1. LIBRARIES: We bring in two "helpers" built into Python
import json
import datetime

# 2. THE FUNCTION: This is our reusable recipe. 
# It takes two ingredients inside the parentheses: phone and amount
def package_mpesa_request(customer_phone, payment_amount):
    
    # Let's use the datetime library to get the exact time right now
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # We build our Dictionary (The Sufuria) using the ingredients
    mpesa_dict = {
        "PhoneNumber": customer_phone,
        "Amount": payment_amount,
        "Time": current_time,
        "Message": "Please pay for your Ugali flour!"
    }
    
    # 3. JSON: We use the json library to translate our Python Dictionary into Internet Text (JSON)
    # The 'indent=4' just makes it look pretty with spaces
    safaricom_json = json.dumps(mpesa_dict, indent=4)
    
    print("--- READY FOR THE INTERNET ---")
    print(safaricom_json)


# --- NOW WE USE THE RECIPE ---
# We can run our function as many times as we want with different customers!

print("Customer 1 is checking out:")
package_mpesa_request("254711222333", 250)

print("\nCustomer 2 is checking out:")
package_mpesa_request("254799888777", 1200)