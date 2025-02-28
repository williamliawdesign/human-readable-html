#!/usr/bin/env python3
"""
HTML Style Preserver and Formatter

This script processes HTML files to make them human-readable (with proper indentation and formatting) while preserving all original styles.
It uses BeautifulSoup to parse and reformat the HTML with proper indentation.

Usage:
    python preserve_style_html.py [input_directory] [output_directory]

If no directories are specified, it will use the current directory for input and create
an 'output' directory for the results.
"""

import os
import sys
import re
from bs4 import BeautifulSoup
from pathlib import Path
import traceback
import html

def format_html(input_file, output_dir):
    """Process an HTML file to make it human-readable while preserving all styles"""
    try:
        # Get input and output paths
        input_path = Path(input_file)
        output_path = Path(output_dir) / input_path.name
        
        print(f"Processing {input_path.name}...")
        
        # Read the HTML content
        with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
            html_content = f.read()
        
        # Parse the HTML with html.parser to preserve the original structure as much as possible
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Format the HTML with proper indentation
        formatted_html = soup.prettify()
        
        # Write the formatted HTML to the output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_html)
        
        print(f"Saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        traceback.print_exc()
        return False

def main():
    """Main function to process HTML files"""
    # Get input and output directories from command line arguments
    if len(sys.argv) >= 3:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
    else:
        input_dir = '.'
        output_dir = './output'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all HTML files in the input directory
    html_files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
    
    if not html_files:
        print(f"No HTML files found in {input_dir}")
        return
    
    # Process each HTML file
    success_count = 0
    for html_file in html_files:
        input_path = os.path.join(input_dir, html_file)
        if format_html(input_path, output_dir):
            success_count += 1
    
    print(f"\nProcessed {success_count} of {len(html_files)} HTML files successfully.")
    print(f"Output saved to {output_dir}")

if __name__ == "__main__":
    main() 