from flask import Flask, request, jsonify

# 1. Create the Flask App (The Reception Desk)
app = Flask(__name__)

# 2. Create the specific door Safaricom will knock on
@app.route('/callback', methods=['POST'])
def mpesa_callback():
    print("\n📩 --- INCOMING MESSAGE FROM SAFARICOM --- 📩")
    
    # Grab the JSON data Safaricom just dropped off
    safaricom_receipt = request.json
    
    # Print it to our terminal so we can read it!
    print(safaricom_receipt)
    
    # Tell Safaricom "Thank you, we received it!" so they don't keep trying
    return jsonify({
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    })

# 3. Start the server! (It will stay awake listening on port 5000)
if __name__ == '__main__':
    print("Receptionist is awake and listening on port 5000...")
    app.run(port=5000)