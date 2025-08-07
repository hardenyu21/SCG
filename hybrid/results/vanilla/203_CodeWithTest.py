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
import unittest
from unittest.mock import patch, MagicMock
import smtplib
class TestCases(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_f225(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = task_func('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    @patch('smtplib.SMTP')
    def test_f225_subject(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = task_func('{"recipient": "names@gmail.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\nJosie Smith\nMugsy Dog Smith')
        
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    
    @patch('smtplib.SMTP')
    def test_no_names(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "names@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text)
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_recepient(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text)
        
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_login(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": ["Name 1", "Name 2"]}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text, email_address="your.email.change@gmail.com", email_password="your.password.change")
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email.change@gmail.com', 'your.password.change')
        # Assert the return value
        self.assertEqual(result, ["Name 1", "Name 2"])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)