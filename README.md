# Dominant Color

A simple Python script to extract the dominant color(s) from an image or all images in a directory.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/csantosr/dominant-color.git
```

2. Navigate to the project directory, create, and activate the virtual environment:
```bash
cd dominant-color
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

To extract the dominant color from an individual image:
```bash
python dominant_color.py /path/to/your/image.jpg
```
The script will print the dominant color in HEX format.

To extract dominant colors from all images in a directory:
```bash
python dominant_color.py /path/to/your/directory/
```
The script will print the dominant color for each image in HEX format, mapping the filename to its dominant color.

If the provided path is neither a recognized image nor a directory, an error message will be displayed.

## License

MIT
