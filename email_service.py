import smtplib
import os
import dotenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv(override=True)

# Sender & Receiver
sender_email = os.getenv("EMAIL_SENDER")
receiver_email = os.getenv("EMAIL_RECIEVER")
app_password = os.getenv("EMAIL_APP_PASSWORD")


def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """Send an email using SMTP."""
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(smtp_user, smtp_password)  # Login to the SMTP server
            server.sendmail(from_email, to_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    """Main entry point for the email service."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Standard port for TLS
    smtp_user = sender_email
    smtp_password = app_password

    send_email(subject, body, receiver_email, sender_email, smtp_server, smtp_port, smtp_user, smtp_password)

if __name__ == "__main__":
    subject = "Test Email from Python"
    body = "This is a test email sent from Python using SMTP."
    
    # Call the main function to send the email
    main()