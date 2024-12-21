from PIL import Image, ImageDraw, ImageFont

# Function to create the project icon
def create_project_icon(project_name, output_file):
    # Canvas size and background color
    width, height = 512, 512
    background_color = "#1e1e2e"
    text_color = "#ffffff"
    accent_color = "#ff6347"  # Accent for the symbol
    
    # Create a blank image with a background color
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Load font
    try:
        font_large = ImageFont.truetype("arial.ttf", 100)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw a circle symbol
    circle_x, circle_y = width // 2, height // 3
    circle_radius = 70
    draw.ellipse(
        (circle_x - circle_radius, circle_y - circle_radius, 
         circle_x + circle_radius, circle_y + circle_radius),
        fill=accent_color,
    )
    
    # Measure the text size for the project name
    text_bbox = draw.textbbox((0, 0), project_name, font=font_large)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Draw the project name
    text_x = (width - text_width) // 2
    text_y = circle_y + circle_radius + 20
    draw.text((text_x, text_y), project_name, fill=text_color, font=font_large)
    
    # Draw subtext (e.g., "GitHub Project")
    subtext = "GitHub Project"
    subtext_bbox = draw.textbbox((0, 0), subtext, font=font_small)
    subtext_width = subtext_bbox[2] - subtext_bbox[0]
    subtext_height = subtext_bbox[3] - subtext_bbox[1]
    
    subtext_x = (width - subtext_width) // 2
    subtext_y = text_y + text_height + 10
    draw.text((subtext_x, subtext_y), subtext, fill=text_color, font=font_small)
    
    # Save the image
    image.save(output_file)
    print(f"Project icon saved as {output_file}")

# Example usage
create_project_icon("CodeMaster", "project_icon.png")
