import re
import smtplib

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS, smtp=None):
    # Regular expression to find names not enclosed in square brackets
    pattern = r'(?<!\[)([A-Za-z\s]+)(?!\])'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Filter out any empty strings that might be matched
    extracted_names = [name.strip() for name in matches if name.strip()]
    
    # Format the email message
    email_message = f"Subject: Extracted Names\n\n" + "\n".join(extracted_names)
    
    # Send the email
    if smtp is None:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(email_address, email_password)
    
    smtp.sendmail(email_address, recepient_address, email_message)
    smtp.quit()
    
    # Return the list of extracted names
    return extracted_names

# Example usage
if __name__ == "__main__":
    extracted_names = task_func()
    print("Extracted Names:", extracted_names)