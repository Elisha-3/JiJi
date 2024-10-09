import requests  # Import the requests library for making HTTP requests
import base64  # Import the base64 library for encoding data
import datetime  # Import the datetime library to work with dates and times
from requests.auth import HTTPBasicAuth  # Import HTTPBasicAuth for basic authentication

def mpesa_payment(amount, phone):
    # Function to handle M-Pesa payments; takes amount and phone number as parameters
    
    # GENERATING THE ACCESS TOKEN
    consumer_key = "8bitK7jaBWyKXIpYAo2oxnjdMUPs8oZ3DdLAEV8fg3v6vsF3"  # Your M-Pesa API consumer key
    consumer_secret = "4FY7DHyjPwQGVVHVkK00pn9AeYhsQTEESwr38INtgQKETz8TK1YNuDXeOrMGG7DR"  # Your M-Pesa API consumer secret
    
    # Authentication URL for generating the access token
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))  # Send a GET request with basic auth
    
    # Get the JSON response containing the access token
    data = r.json()  
    access_token = "Bearer" + ' ' + data['access_token']  # Format the access token with "Bearer" prefix

    # GETTING THE PASSWORD
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')  # Generate a timestamp in the required format
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Your M-Pesa API passkey
    business_short_code = "174379"  # Your business short code
    data = business_short_code + passkey + timestamp  # Concatenate business short code, passkey, and timestamp
    encoded = base64.b64encode(data.encode())  # Encode the concatenated data to base64
    password = encoded.decode('utf-8')  # Decode the base64-encoded data to get the password

    # BODY OR PAYLOAD
    payload = {
        "BusinessShortCode": "174379",  # Business short code
        "Password": "{}".format(password),  # The encoded password
        "Timestamp": "{}".format(timestamp),  # The timestamp
        "TransactionType": "CustomerPayBillOnline",  # Type of transaction
        "Amount": amount,  # Amount to be paid (passed as a parameter)
        "PartyA": phone,  # The phone number of the payer
        "PartyB": "174379",  # Business short code (receiver)
        "PhoneNumber": phone,  # The payer's phone number again for reference
        "CallBackURL": "https://modcom.co.ke/job/confirmation.php",  # URL to receive payment confirmation
        "AccountReference": "account",  # Reference for the transaction
        "TransactionDesc": "account"  # Description of the transaction
    }

    # POPULATING THE HTTP HEADER
    headers = {
        "Authorization": access_token,  # Set the Authorization header with the access token
        "Content-Type": "application/json"  # Specify the content type as JSON
    }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # URL for the M-Pesa STK Push request

    response = requests.post(url, json=payload, headers=headers)  # Send a POST request with the payload and headers
    print(response.text)  # Print the response from the API
