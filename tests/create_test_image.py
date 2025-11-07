#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file generator: Creates a sample image with text for OCR testing.

Copyright (c) 2025 NJC Software LLC
Licensed under the MIT License. See LICENSE file for details.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_image():
    # Create a new image with white background
    width = 800
    height = 600
    background_color = 'white'
    img = Image.new('RGB', (width, height), background_color)
    
    # Get drawing context
    draw = ImageDraw.Draw(img)
    
    # Add text to the image
    text_color = 'black'
    try:
        # Try to use Arial font, fall back to default if not available
        font = ImageFont.truetype("Arial", 40)
    except:
        font = ImageFont.load_default()

    # Draw multiple lines of text
    texts = [
        "Sample Image for OCR Testing",
        "This image contains text",
        "that should be readable",
        "by OCR software.",
        "Testing 123"
    ]
    
    y_position = 100
    for text in texts:
        # Get text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        # Center text horizontally
        x_position = (width - text_width) / 2
        # Draw text
        draw.text((x_position, y_position), text, fill=text_color, font=font)
        y_position += 80

    # Save the image
    img.save("tests/test_files/sample_image.png")

if __name__ == "__main__":
    create_sample_image()