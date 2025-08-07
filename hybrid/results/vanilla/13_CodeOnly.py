import subprocess
import ftplib
import os

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
    except Exception as e:
        raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")

    try:
        # Login to the FTP server
        ftp.login(user=ftp_user, passwd=ftp_password)
    except Exception as e:
        raise Exception(f"Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}")

    try:
        # Change to the specified directory
        ftp.cwd(ftp_dir)
    except Exception as e:
        raise Exception(f"Failed to change to directory {ftp_dir} on server {ftp_server}: {str(e)}")

    # List all files in the directory
    files = ftp.nlst()

    # Attempt to download each file using wget
    downloaded_files = []
    for file in files:
        try:
            # Construct the wget command
            command = [
                'wget',
                f'ftp://{ftp_user}:{ftp_password}@{ftp_server}{ftp_dir}/{file}',
                '-P', '.'
            ]
            # Execute the wget command
            subprocess.run(command, check=True)
            downloaded_files.append(file)
        except subprocess.CalledProcessError as e:
            print(f"Failed to download file {file}: {str(e)}")

    # Close the FTP connection
    ftp.quit()

    return downloaded_files