pip install opencv-python
import cv2
import numpy as np

import matplotlib.pyplot as plt

image = cv2.imread('/content/drive/MyDrive/Servants_of_The_Most_High/Kingdom_with_A.I._Project/DSS Scrolls/Isaiah/tiles/9_0_0.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to make text clearer (adaptive thresholding can also be tried)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

extracted_characters = []

cv2.imwrite('/content/drive/MyDrive/Servants_of_The_Most_High/Kingdom_with_A.I._Project/WorkBooks/outputChars/Jan9_2025/dssoutput.png', binary)

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(f'Contour {i} has area: {area}')

# Define a minimum area threshold (this can be adjusted based on your image)
min_contour_area = 100  # Adjust this value as needed

# Loop through the contours and filter by min defined area
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)

    if area >= min_contour_area:  # Only keep contours with area larger than the threshold
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract the character using the bounding box
        char_image = binary[y:y+h, x:x+w]
        extracted_characters.append(char_image)
        cv2.imwrite(f'/content/drive/MyDrive/Servants_of_The_Most_High/Kingdom_with_A.I._Project/WorkBooks/embedfolder/characters/character_{i}.png', char_image)

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)

    if area >= min_contour_area:  # Only keep contours with area larger than the threshold
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract the character using the bounding box
        char_image = binary[y:y+h, x:x+w]
        extracted_characters.append(char_image)

        # Save each character image
        # i.e cv2.imwrite(f'/content/snaps/out2/character_{i}.png', char_image)
        cv2.imwrite(f'/content/embedFolder/characters/character_{i}.png', char_image)

# Display extracted characters
fig, axes = plt.subplots(1, len(extracted_characters), figsize=(15, 5))
for ax, char_img in zip(axes, extracted_characters):
    ax.imshow(char_img, cmap='gray')
    ax.axis('off')
plt.show()

import os

# Directory containing the images
# Check if this directory exists
image_directory = '/content/embedFolder/tformtiles'  

# Output directory for saved results
output_directory = '/content/embedFolder/char'

# If the directory doesn't exist, create it or update the path
if not os.path.exists(image_directory):
    # Option 1: Create the directory if it doesn't exist
    # os.makedirs(image_directory, exist_ok=True)  
    # print(f"Created directory: {image_directory}")

    # Option 2: Update the path to the correct directory
    image_directory = '/content/drive/MyDrive/Servants_of_The_Most_High/Kingdom_with_A.I._Project/WorkBooks/outputChars/Jan9_2025/'  # Replace with your actual image directory
    print(f"Updated image_directory to: {image_directory}")

# Make sure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop over all files in the image directory
for filename in os.listdir(image_directory):
    if filename.endswith('.webp'):  # Process only .webp files or change as needed
        image_path = os.path.join(image_directory, filename)

        # Read the image
        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        extracted_characters = []

        # Process contours
        min_contour_area = 100  # Adjust as necessary
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area >= min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                char_image = binary[y:y+h, x:x+w]
                extracted_characters.append(char_image)
                # Save each character image
                cv2.imwrite(os.path.join(output_directory, f'{filename}_character_{i}.png'), char_image)

        # Display extracted characters
        fig, axes = plt.subplots(1, len(extracted_characters), figsize=(15, 5))
        for ax, char_img in zip(axes, extracted_characters):
            ax.imshow(char_img, cmap='gray')
            ax.axis('off')
        plt.show()

cd /content/drive/MyDrive/'Servants_of_The_Most_High/Kingdom_with_A.I._Project'/WorkBooks

cd /content/embedFolder

!zip -r char.zip char
