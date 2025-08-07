import json
import smtplib
from email.mime.text import MIMEText

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    if input_data is None:
        raise ValueError("Input data is required")

    # Parse the JSON data
    try:
        data = json.loads(input_data)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON data") from e

    # Extract recipient email addresses and names
    recipients = []
    for item in data.get("recipients", []):
        email = item.get("email")
        name = item.get("name")
        if email and name:
            recipients.append((email, name))

    # Extract names only
    names = [name for _, name in recipients]

    # Prepare the email message
    subject = "Extracted Names"
    body = "\n".join(names)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = ", ".join(email for email, _ in recipients)

    # Send the email
    if smtp is None:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(email_address, email_password)

    try:
        smtp.sendmail(email_address, [email for email, _ in recipients], msg.as_string())
    finally:
        if smtp is not None:
            smtp.quit()

    return names