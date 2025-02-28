# HTML to Readable HTML Converter 📄

This tool processes and converts HTML files from SingleFile pages to readable HTML files while preserving styles and scripts.

## Features ✨

- Cleans up complex HTML files while preserving functionality
- Removes unnecessary attributes and UI clutter
- Preserves styles, scripts, and interactive elements
- Organizes content into clear, readable sections
- Maintains important data like haplogroup names, age estimates, and geographic information

## Requirements 📋

- Python 3.6 or higher
- BeautifulSoup4 library
- html5lib parser
- lxml parser

## Installation 🔧

1. Make sure you have Python 3 installed on your system
2. Set up a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate  # On Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install beautifulsoup4 html5lib lxml
```

## Usage 🚀

### Basic Usage

Run the script from the command line:

```bash
python3 preserve_style_html.py
```

This will look for HTML files in the current directory and save the processed output to a new `output` directory. If no HTML files are found in the current directory, the script will report "No HTML files found".

### Advanced Usage (Recommended)

You can specify input and output directories, which is the recommended approach:

```bash
python3 preserve_style_html.py original-files output
```

This command will:
1. Take all HTML files from the `original-files` directory
2. Process them to make them human-readable with proper indentation
3. Save the processed files to the `output` directory

## What the Script Does 🛠️

The script performs the following operations:

1. **Cleans the HTML**:
   - Parses HTML with BeautifulSoup
   - Preserves the original structure
   - Makes the HTML more human-readable with proper indentation

2. **Formatting Process**:
   - Maintains the complete HTML structure
   - Adds proper indentation for readability
   - Preserves all original styles and scripts

3. **Output**:
   - Creates formatted HTML files in the output directory
   - Preserves original filenames
   - Maintains all functionality of the original files

## Example 📊

Input: `your_page.html` (Downloaded SingleFile HTML page)

Output: `your_page.html` in the output directory with:
- Clean, properly indented HTML structure
- Preserved styles and functionality
- Better readability for human inspection

## Troubleshooting 🔍

If you encounter issues:

1. Make sure the HTML files are properly formatted
2. Check that you have the required dependencies installed
3. Verify file permissions for reading input and writing output
4. If you see "command not found: python", try using `python3` instead

## License 📜

This project is available under the MIT License. 