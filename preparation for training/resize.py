import os
from PIL import Image

def change_resolution_in_folder(folder, new_resolution):
    # Iterate through all files in the specified folder
    for file in os.listdir(folder):
        if file.endswith(".jpg") or file.endswith(".png"):  # Check if the file is an image
            image_path = os.path.join(folder, file)

            # Open the image
            image = Image.open(image_path)

            # Change the resolution
            resized_image = image.resize(new_resolution)

            # Save the resized image, replacing the original
            resized_image.save(image_path)

# Example of usage
image_folder = "C:\\Users\\Nikita\\Desktop\\dataset_1.7\\valid\\images"
new_resolution = (640, 640)  # Specify the new width and height values
change_resolution_in_folder(image_folder, new_resolution)
