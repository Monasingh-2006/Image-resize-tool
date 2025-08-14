import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    resized_img = img.resize((width, height))
                    resized_img.save(output_path)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Set folder paths and size here
resize_images("images/original", "images/resized", 300, 300)

print("Done! Check the 'images/original folder for output.")
