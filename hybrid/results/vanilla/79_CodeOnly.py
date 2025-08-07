import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create an in-memory bytes buffer to hold the ZIP file
    buffer = io.BytesIO()
    
    # Create a ZIP file in the buffer
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            # Ensure the file path is secure and within the allowed directory
            if not file_path.startswith(settings.MEDIA_ROOT):
                raise ValueError("File path is not within the allowed directory.")
            
            # Add the file to the ZIP archive
            zipf.write(file_path, arcname=file_path[len(settings.MEDIA_ROOT):])
    
    # Seek to the beginning of the buffer
    buffer.seek(0)
    
    # Create a FileResponse with the ZIP file as an attachment
    response = FileResponse(buffer, as_attachment=True, filename='files.zip')
    
    return response