import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def send_email(content, recipient_email="sahanr.silva@proton.me"):
    config = load_config('app/config.json')
    sender_email = config['email']['sender_email']
    sender_password = config['email']['sender_password']
    
    subject = "Notification"
    body = content

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  
        server.login(sender_email, sender_password)
        text = message.as_string()
        
        server.sendmail(sender_email, recipient_email, text)  
        print(f"OTP sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

