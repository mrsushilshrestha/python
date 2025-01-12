import os
from datetime import datetime

# Define the directory containing the images
directory_to_watch = r"100-day-Challange\image"

# Define the path for the Markdown file to store image URLs
md_file_path = "program-snap.md"

# File extensions to monitor (you can add other formats if needed)
image_extensions = ('.png', '.jpg', '.jpeg')

# Function to get the creation time of a file and sort images by it
def get_image_creation_time(file_path):
    # Get the creation time of the file
    return os.path.getctime(file_path)

# Function to scan the directory and generate markdown links for each image file
def scan_and_generate_markdown():
    # Check if the directory exists
    if not os.path.exists(directory_to_watch):
        print(f"The directory {directory_to_watch} does not exist. Please create it.")
        return
    
    # Initialize a list to store image file info (filename and creation time)
    image_files_info = []

    # Loop through all files in the image directory
    for filename in os.listdir(directory_to_watch):
        # Check if the file is an image (based on the extension)
        if filename.lower().endswith(image_extensions):
            file_path = os.path.join(directory_to_watch, filename)
            creation_time = get_image_creation_time(file_path)
            image_files_info.append((filename, creation_time))
    
    # Sort images by their creation time (ascending order)
    image_files_info.sort(key=lambda x: x[1])

    # Initialize a list to store markdown links
    markdown_links = []

    # Loop through each image file and create the markdown format
    for i, (filename, _) in enumerate(image_files_info, start=1):
        # Construct the raw GitHub URL for the image file
        file_url = f"https://raw.githubusercontent.com/mrsushilshrestha/python/main/100-day-Challange/image/{filename}"
        # Append the formatted markdown link to the list
        markdown_links.append(f"## Snapshot {i}\n![Code Snapshot {i}]({file_url})\n")
    
    # Save the markdown links to the program-snap.md file
    with open(md_file_path, "w") as md_file:
        md_file.write("Here are some snapshots of my code:\n\n")
        for link in markdown_links:
            md_file.write(link + "\n")
    
    print(f"Successfully updated {md_file_path} with the image links.")

# Run the program
if __name__ == "__main__":
    scan_and_generate_markdown()
