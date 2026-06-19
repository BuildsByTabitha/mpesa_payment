import requests
import base64
from datetime import datetime
import auth  # This imports YOUR auth.py file so we can borrow the VIP Wristband!

def trigger_stk_push(phone_number, amount):
    print(f" STK Push for {phone_number}...")

    # 1. Get the VIP Wristband from your auth file
    access_token = auth.get_access_token()
    
    if access_token is None:
        print("❌ Could not get access token. Stopping.")
        return

    # 2. Setup Safaricom's Universal Sandbox Test Credentials
    # (These are public test keys Safaricom provides to all developers)
    business_shortcode = "174379"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    
    # 3. Generate the Timestamp (YearMonthDayHourMinuteSecond)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # 4. Generate the Password (Scramble the Shortcode + Passkey + Timestamp)
    data_to_encode = business_shortcode + passkey + timestamp
    encoded_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

    # 5. The door we are knocking on for the STK Push
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    # 6. The Header (Showing our VIP Wristband and our Fake Mustache!-prevent the firewall frm denying us access )
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" # The Fake Mustache
    }
    # 7. The Dictionary (The exact package Safaricom demands)
    payload = {
        "BusinessShortCode": business_shortcode,
        "Password": encoded_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,          # The person paying
        "PartyB": business_shortcode,    # The business receiving
        "PhoneNumber": phone_number,
        "CallBackURL": "https://webhook.site/62a471a6-604b-4788-b9b9-cca74e8e41c9", # Reception hosted in a server where final receipt is sent
        "AccountReference": "BuildsByTabitha",
        "TransactionDesc": "Payment for coding lessons"
    }

    # 8. Send the Delivery Guy (requests) to drop off the package!
    print("Sending package to Safaricom\n")
    response = requests.post(api_url, json=payload, headers=headers)

    print("SAFARICOM STK PUSH RESPONSE")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print(f"Status Code: {response.status_code}")
        print("Safaricom sent raw text instead of JSON:")
        print(response.text)
# --- RUN THE RECIPE ---
# ACTUAL Safaricom phone number (Format: 2547... or 2541...)
my_number = "254107675856" 

# Asking the customer for 1 Ksh
trigger_stk_push(my_number, 5)