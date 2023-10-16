import os
import sys
from PIL import Image
from collections import Counter

def rgb_to_hex(rgb):
    """Converts an RGB tuple to its HEX representation."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_dominant_color(image_path):
    """Returns the dominant color in the image in HEX format, skipping gray colors."""

    image = Image.open(image_path)
    image = image.resize((200, 200))  # Reducing the size for faster processing

    pixels = list(image.getdata())

    # Handle grayscale images
    if isinstance(pixels[0], int):
        # Convert grayscale values to RGB tuples
        pixels = [(pixel, pixel, pixel) for pixel in pixels]

    # Remove alpha if exists
    elif len(pixels[0]) == 4:
        pixels = [(r, g, b) for (r, g, b, a) in pixels if a > 128]

    color_count = Counter(pixels)
    
    # Get the most common colors and skip grays
    for color, _ in color_count.most_common():
        r, g, b = color
        if r != g or r != b:  # If not gray
            return rgb_to_hex(color)

    # If all colors are gray, just return the dominant gray
    return rgb_to_hex(color_count.most_common(1)[0][0])



def process_directory(directory_path):
    """Processes each image in the directory and returns a dictionary
    of filename-to-dominant-color mappings."""
    
    color_map = {}
    
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(directory_path, filename)
            color_map[filename] = get_dominant_color(file_path)
            
    return color_map

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a single argument: path to an image or directory.")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if os.path.isfile(input_path) and input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"Dominant color: {get_dominant_color(input_path)}")
    elif os.path.isdir(input_path):
        dominant_colors = process_directory(input_path)
        for filename, color in dominant_colors.items():
            print(f"{filename}: {color}")
    else:
        print("Error: Provided path is not a recognized image or directory.")
