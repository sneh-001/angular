
import os
import zipfile
from datetime import datetime

def create_zip_from_folder_with_timestamp(folder_path, zip_filename_prefix="archive"):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  
    zip_filename = f"{zip_filename_prefix}_{timestamp}.zip"  
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)

        print(f"Successfully created zip archive: {zip_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

folder_to_zip = "dist"  
zip_prefix = "angular_build"     
create_zip_from_folder_with_timestamp(folder_to_zip, zip_prefix)
