import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    try:
        # Check if the directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError(f"The directory '{dir}' does not exist.")
        
        # List files in the directory
        files = os.listdir(dir)
        files_list = "\n".join(files)
        
        # Create the email content
        subject = "List of Files in Directory"
        content = f"The following files are in the directory '{dir}':\n\n{files_list}"
        
        # Create the email message
        message = Mail(
            from_email='your-email@example.com',  # Replace with your email
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=content
        )
        
        # Send the email using SendGrid
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        # Check if the email was sent successfully
        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return False
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
        raise HTTPError(http_error)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception(e)