import os
from datetime import datetime

# Path to the image folder in the repository
image_folder = "C:/python/100-day-Challange/image"  # Update with your actual folder path

# Path to the HTML gallery file
html_file = "C:/python/100-day-Challange/image-gallery.html"  # Update with your actual file path

# GitHub repository base URL
repo_url = "https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/"

# Function to generate image gallery HTML
def generate_gallery():
    # Scan the folder and get image files
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Sort the images by their modified date
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_folder, x)))
    
    # Create the base HTML template
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Grid Gallery</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .gallery-container { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; width: 90%; max-width: 1200px; background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
            .gallery-item { position: relative; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease; }
            .gallery-item img { width: 100%; height: auto; border-radius: 10px; object-fit: cover; }
            .gallery-item:hover { transform: scale(1.05); }
            .image-caption { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: rgba(0, 0, 0, 0.6); color: white; padding: 10px 20px; font-size: 18px; border-radius: 5px; opacity: 0; transition: opacity 0.3s ease; }
            .gallery-item:hover .image-caption { opacity: 1; }
            @media (max-width: 1200px) { .gallery-container { grid-template-columns: repeat(3, 1fr); } }
            @media (max-width: 768px) { .gallery-container { grid-template-columns: repeat(2, 1fr); } }
            @media (max-width: 480px) { .gallery-container { grid-template-columns: 1fr; } }
        </style>
    </head>
    <body>

    <div class="gallery-container">
    """

    # Add images to the gallery section
    for index, image_file in enumerate(image_files):
        image_url = repo_url + image_file
        image_caption = f"Snapshot {index + 1}"
        html_content += f"""
        <div class="gallery-item">
            <img src="{image_url}" alt="{image_caption}">
            <div class="image-caption">{image_caption}</div>
        </div>
        """

    # Close the gallery container and HTML tags
    html_content += """
    </div>

    </body>
    </html>
    """

    # Write the updated HTML content to the file
    with open(html_file, "w") as file:
        file.write(html_content)
    print(f"Gallery updated successfully! Check {html_file}")

# Call the function to update the gallery
generate_gallery()
