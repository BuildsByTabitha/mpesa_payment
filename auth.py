import requests
from requests.auth import HTTPBasicAuth
import config

def get_access_token():
    print("Asking Safaricom for Access Token...")
    
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    try:
        response = requests.get(
            api_url,
            auth=HTTPBasicAuth(config.MPESA_CONSUMER_KEY, config.MPESA_CONSUMER_SECRET)
        )
        
        safaricom_reply = response.json()
        
        # HERE IS THE FIX: We reach into the dictionary and pull out ONLY the token string!
        my_access_token = safaricom_reply["access_token"]
        
        print("\n✅ Access Token successfully extracted!")
        print(f"My VIP Wristband is: {my_access_token}") # This should print ONLY the letters now!The rest is not issually needed
        
        # Return ONLY the token string
        return my_access_token
        
    except Exception as e:
        print(f"❌ Failed to get token. Error: {e}")
        return None

# We run the function and save the returned token into a variable
token = get_access_token()