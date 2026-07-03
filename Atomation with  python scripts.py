import os
import shutil

source_folder = "source"
destination_folder = "destination"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.copy(os.path.join(source_folder, file), destination_folder)
        print(file, "copied successfully!")

print("All JPG files have been copied.")