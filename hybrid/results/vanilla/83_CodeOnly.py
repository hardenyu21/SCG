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