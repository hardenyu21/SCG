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
import unittest
from unittest.mock import patch, MagicMock
import smtplib
class TestCases(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_f225(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = task_func()
        
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
        result = task_func()
        
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
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text)
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\n')
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_recepient(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text, recepient_address='change@gmail.com')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'change@gmail.com', 'Subject: Extracted Names\n\n')
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_login(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text, email_address="your.email.change@gmail.com", email_password="your.password.change")
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email.change@gmail.com', 'your.password.change')
        # Assert the return value
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)