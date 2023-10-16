# Dominant Color

A simple Python script to extract the dominant color(s) from an image.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/csantosr/dominant-color.git
```

1. Navigate to the project directory, create and activate the virtual environment:
```bash
cd dominant-color
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Replace the image path in `dominant_color.py` line 39 and run:
```bash
python dominant_color.py
```
The script will print the dominant color in HEX format.

## License

MIT
