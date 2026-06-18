import requests
from requests.auth import HTTPBasicAuth
import config # This imports the config.py file you just made!

def get_access_token():
    print("Asking Safaricom for the VIP Access Token...")
    
    # This is the exact door Safaricom tells us to knock on for a token
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    # We use the 'requests' delivery guy to go to the URL.
    # Safaricom requires us to present our ID and Password using "Basic Authentication"
    response = requests.get(
        api_url,
        auth=HTTPBasicAuth(config.MPESA_CONSUMER_KEY, config.MPESA_CONSUMER_SECRET)
    )
    
    # Sometimes if keys are completely fake, Safaricom sends back an error webpage or raw text instead of JSON.
    # We use a 'try/except' block so Python doesn't crash if that happens.
    try:
        # Try to take the receipt Safaricom hands back and translate it using JSON
        safaricom_reply = response.json()
        
        print("\n--- SAFARICOM'S REPLY (JSON) ---")
        print(safaricom_reply)
        
    except requests.exceptions.JSONDecodeError:
        # If it fails to translate to JSON, we catch the error and print the raw text instead
        print("\n--- SAFARICOM'S REPLY (RAW TEXT/ERROR) ---")
        print(f"Status Code: {response.status_code}")
        print("Safaricom didn't return JSON. Here is exactly what they said:")
        print(response.text)

# Run the recipe!
get_access_token()