import zipfile

# Define the file path
file_path = r"C:\Users\Jainam\PycharmProjects\FaceRecognition\Lib\site-packages\tensorflow\python\_pywrap_tensorflow_internal.pyd"

# Define the name for the ZIP archive
zip_file_name = "file_archive.zip"

# Create a ZIP archive
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add the file to the archive
    zipf.write(file_path, arcname="_pywrap_tensorflow_internal.pyd")