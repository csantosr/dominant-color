from PIL import Image
from collections import Counter

def rgb_to_hex(rgb):
    """Converts an RGB tuple to its HEX representation."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_dominant_color(image_path, k=1):
    """
    Returns the dominant color(s) in the image in HEX format.

    Parameters:
    - image_path: The path to the image.
    - k: The number of dominant colors to return.

    Returns:
    - A list of HEX color strings.
    """

    # Open the image and resize for faster processing
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Reducing the size for faster processing

    # Get image pixels
    pixels = list(image.getdata())

    # Remove alpha if exists
    if len(pixels[0]) == 4:
        pixels = [(r, g, b) for (r, g, b, a) in pixels if a > 128]

    # Get the most common colors
    color_count = Counter(pixels)
    dominant_colors = color_count.most_common(k)

    # Convert RGB to HEX and return
    return [rgb_to_hex(color[0]) for color in dominant_colors]

if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    dominant_colors = get_dominant_color(image_path)
    print(dominant_colors)
