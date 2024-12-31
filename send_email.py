import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from twilio.rest import Client

# Twilio account credentials
account_sid = 'twilio_account_id'
auth_token = 'twilio_auth_token'
twilio_phone_number = 'twilio_phone_number'
recipient_number = 'recipent_phone_number'

# Configuration
sender_email = 'anshujpr102@gmail.com'
sender_password = 'email_password_here'
recipient_email = 'anshujpr103@gmail.com'

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

def send_email(subject, body):
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in and send the email
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the server
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Main function to get subject and body from command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_notification.py <subject> <message>")
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2]

    send_email(subject, body)
    send_sms(body)

