from PIL import Image
import codecs
import pytesseract

IMAGE_PATH = "image.png"

def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    try:
        # Open the image file
        with Image.open(filename) as img:
            # Try to extract text using OCR
            try:
                text = pytesseract.image_to_string(img)
                # Convert the extracted text encoding
                try:
                    text = text.encode(from_encoding).decode(to_encoding)
                    return text
                except (UnicodeDecodeError, LookupError) as e:
                    raise ValueError(f"Encoding conversion error: {e}")
            except Exception as e:
                print(f"OCR extraction failed: {e}")

            # If OCR fails, try to extract text from the image comment
            try:
                comment = img.info.get('comment', '')
                # Convert the comment encoding
                try:
                    comment = comment.encode(from_encoding).decode(to_encoding)
                    return comment
                except (UnicodeDecodeError, LookupError) as e:
                    raise ValueError(f"Encoding conversion error: {e}")
            except Exception as e:
                print(f"Comment processing failed: {e}")

    except Exception as e:
        print(f"Error opening image file: {e}")

    # If both OCR and comment processing fail, return an empty string
    return ""

# Example usage
if __name__ == "__main__":
    result = task_func()
    print("Extracted text or comment:", result)