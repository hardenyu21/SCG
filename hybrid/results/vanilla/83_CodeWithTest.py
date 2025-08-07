from flask import Flask, render_template_string
from flask_mail import Mail, Message

def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    # Initialize the Flask application
    app = Flask(__name__, template_folder=template_folder)

    # Configure the Flask-Mail settings
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password

    # Initialize Flask-Mail
    mail = Mail(app)

    # Define a route to send a test email
    @app.route('/send-test-email')
    def send_test_email():
        # Create a message object
        msg = Message("Test Email",
                      sender=smtp_user,
                      recipients=["recipient@example.com"])
        
        # Render a simple HTML template for the email body
        msg.html = render_template_string("<h1>Hello, this is a test email!</h1>")
        
        # Send the email
        mail.send(msg)
        
        return "Test email sent!"

    # Return the Flask application instance
    return app
import unittest
from unittest.mock import patch
from flask import Flask
from flask_mail import Mail
class TestCases(unittest.TestCase):
    def setUp(self):
        # Constants used for testing
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587
        self.smtp_user = 'user@example.com'
        self.smtp_password = 'password'
        self.template_folder = 'templates'
        # Create the app with test configurations
        self.app = task_func(self.smtp_server, self.smtp_port, self.smtp_user, self.smtp_password, self.template_folder)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    def test_app_instance(self):
        """Test if the function returns a Flask app instance."""
        self.assertIsInstance(self.app, Flask)
    def test_mail_config(self):
        """Test if the mail configuration is set correctly."""
        self.assertEqual(self.app.config['MAIL_SERVER'], self.smtp_server)
        self.assertEqual(self.app.config['MAIL_PORT'], self.smtp_port)
        self.assertEqual(self.app.config['MAIL_USERNAME'], self.smtp_user)
        self.assertEqual(self.app.config['MAIL_PASSWORD'], self.smtp_password)
    @patch.object(Mail, 'send')
    def test_send_mail_route(self, mock_mail_send):
        """Test if the send_mail route triggers the mail sending."""
        response = self.client.get('/send_mail')
        self.assertEqual(response.status_code, 200)
        mock_mail_send.assert_called_once()
    def test_send_mail_functionality(self):
        """Test the functionality of sending an email."""
        with patch('flask_mail.Mail.send') as mock_mail_send:
            response = self.client.get('/send_mail')
            self.assertEqual(response.status_code, 200)
            mock_mail_send.assert_called_once()
            args, kwargs = mock_mail_send.call_args
            message = args[0]
            self.assertEqual(message.subject, 'Hello')
            self.assertEqual(message.sender, 'from@example.com')
            self.assertEqual(message.recipients, ['to@example.com'])
    def test_smtp_configuration(self):
        """Ensure SMTP settings are correctly configured."""
        # Since we have already tested the configuration in setUp, this test could be redundant
        # Or it could be kept for isolated testing of SMTP configurations without setup
        self.assertEqual(self.app.config['MAIL_SERVER'], self.smtp_server)
        self.assertEqual(self.app.config['MAIL_PORT'], self.smtp_port)
        self.assertEqual(self.app.config['MAIL_USERNAME'], self.smtp_user)
        self.assertEqual(self.app.config['MAIL_PASSWORD'], self.smtp_password)
        self.assertEqual(self.app.config['MAIL_USE_TLS'], True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)