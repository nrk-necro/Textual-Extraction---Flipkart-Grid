import cv2
import numpy as np

# Load the image
image = cv2.imread('8d2ee3b5-6c02-42e9-b9ab-04deb5b91365_1665215133177.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Adjusting global threshold (increase/decrease 150 based on the image)
_, binary_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

# Adaptive thresholding for uneven lighting
adaptive_thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)

"""
"""
# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
"""
# Apply binary thresholding
_, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY)

# Define kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# Apply dilation and erosion
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
"""
# Final result
cv2.imshow('Preprocessed Image', blurred_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

