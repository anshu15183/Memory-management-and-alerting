from twilio.rest import Client

# Twilio account credentials
account_sid = 'twilio_account_id'
auth_token = 'twilio_auth_token'
twilio_phone_number = 'twilio_phone_number'
recipient_number = 'recipent_phone_number'

def send_sms(message):
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Send SMS
        message = client.messages.create(
            from_=twilio_phone_number,
            body=message,
            to=recipient_number
        )
        
        print(f"SMS sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 send_sms.py <message>")
        sys.exit(1)
    
    # Get the message to send from command-line arguments
    message_to_send = sys.argv[1]
    send_sms(message_to_send)

