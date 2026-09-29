import os
import shutil

source_folder = "source"
destination_folder = "destination"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

print("All JPG files moved successfully!")