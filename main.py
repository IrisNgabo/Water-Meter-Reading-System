import cv2
import pytesseract

# Path to Tesseract executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

# Read the image
image = cv2.imread('image-reading.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR using Tesseract
text = pytesseract.image_to_string(gray_image)

# Print the extracted text
print("Extracted Text:", text.strip())
