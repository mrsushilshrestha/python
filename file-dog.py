import os

# Define the directory containing the images
directory_to_watch = r"C:\python\100-day-Challange\image"

# Define the path for the Markdown file to store image URLs
md_file_path = "program-snap.md"

# File extensions to monitor (you can add other formats if needed)
image_extensions = ('.png', '.jpg', '.jpeg')

# Function to scan the directory and generate markdown links for each image file
def scan_and_generate_markdown():
    # Check if the directory exists
    if not os.path.exists(directory_to_watch):
        print(f"The directory {directory_to_watch} does not exist. Please create it.")
        return
    
    # Initialize a list to store markdown links
    markdown_links = []

    # Loop through all files in the image directory
    image_files = [f for f in os.listdir(directory_to_watch) if f.lower().endswith(image_extensions)]
    
    # Sort the files alphabetically (if you want a specific order)
    image_files.sort()

    # Loop through each image file and create the markdown format
    for i, filename in enumerate(image_files, start=1):
        # Construct the GitHub URL for the image file
        file_url = f"https://github.com/mrsushilshrestha/python/blob/main/100-day-Challange/image/{filename}"
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
