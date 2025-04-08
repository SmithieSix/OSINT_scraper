import smtplib
from email.mime.text import MIMEText
from config import EMAIL

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL["sender"]
    msg["To"] = EMAIL["recipient"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL["sender"], EMAIL["password"])
        server.send_message(msg)
