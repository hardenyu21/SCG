import smtplib
from email.message import EmailMessage
import getpass

SERVER_ADDRESS = "localhost"
SERVER_PORT = 25
BUFFER_SIZE = 1024
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def task_func(client_socket):
    # Receive message from client socket
    message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    
    # Get sender's email, recipient's email, and sender's email password
    sender_email = input("Enter sender's email: ")
    recipient_email = input("Enter recipient's email: ")
    sender_password = getpass.getpass("Enter sender's email password: ")
    
    # Create an email message
    email = EmailMessage()
    email.set_content(message)
    email['Subject'] = 'Message from Client Socket'
    email['From'] = sender_email
    email['To'] = recipient_email
    
    # Send the email via SMTP server
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(email)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    return None