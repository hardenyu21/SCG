import os
from flask import Flask
from flask_mail import Mail

def task_func(app):
    # Default mail configuration
    default_mail_config = {
        'MAIL_SERVER': 'smtp.example.com',
        'MAIL_PORT': 587,
        'MAIL_USE_TLS': True,
        'MAIL_USERNAME': 'user@example.com',
        'MAIL_PASSWORD': 'password'
    }

    # Retrieve mail configuration from environment variables
    mail_config = {
        'MAIL_SERVER': os.getenv('MAIL_SERVER', default_mail_config['MAIL_SERVER']),
        'MAIL_PORT': int(os.getenv('MAIL_PORT', default_mail_config['MAIL_PORT'])),
        'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', str(default_mail_config['MAIL_USE_TLS'])).lower() in ['true', '1', 't'],
        'MAIL_USERNAME': os.getenv('MAIL_USERNAME', default_mail_config['MAIL_USERNAME']),
        'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD', default_mail_config['MAIL_PASSWORD'])
    }

    # Update app configuration with mail settings
    app.config.update(mail_config)

    # Initialize Flask-Mail
    mail = Mail(app)

    return mail, mail_config

# Example usage:
# app = Flask(__name__)
# mail, mail_config = task_func(app)
# print(mail_config)