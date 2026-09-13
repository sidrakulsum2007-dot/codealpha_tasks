import os
import shutil

# Folder containing the original image files
source_folder = "source_folder"

# Folder where the image files will be moved
destination_folder = "destination_folder"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check all files in the source folder
for filename in os.listdir(source_folder):

    # Move JPG and JPEG files
    if filename.lower().endswith((".jpg", ".jpeg")):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)

        print("Moved:", filename)

print("Automation completed successfully!")