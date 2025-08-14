🖼️ Simple Image Resizer (Python)

This is a lightweight Python script to batch resize images in a folder using the Pillow library.

✅ Features

Resize all images in a folder to a fixed size

Supports JPG, PNG, BMP, GIF, and JPEG

Easy to configure paths and size

Saves resized images to an output folder

🛠️ Requirements

Python 3.x

Pillow library

Install Pillow:

pip install Pillow

📂 Folder Structure
images/
├── original/   # Input images here
└── resized/    # Output images will be saved here

▶️ How to Use

Place your images in the images/original folder.

Set the desired width and height in the script.

Run the script:

python resizer.py


Resized images will be saved to images/resized.

🧪 Example Output

Original: 1200x800 → Resized: 300x300

Input: images/original/pic1.jpg

Output: images/resized/pic1.jpg

📄 Script Snippet
resize_images("images/original", "images/resized", 300, 300)


Change folder names and size as needed.

📌 Notes

Only processes .jpg, .jpeg, .png, .bmp, .gif

your.email@example.com

Let me know if you want this formatted as a downloadable file or need a version with CLI support.
