import numpy as np
import cv2

def process_image(image_path, output_path):
    # Read the image from the provided path
    frame = cv2.imread(image_path)
    
    # Convert the image to grayscale
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to the grayscale image
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Draw contours on the original image
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filter out small contours
            approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)  # Draw green contours

    # Save the result to the output path
    cv2.imwrite(output_path, frame)
    
    # Show the images for reference (optional)
    cv2.imshow('Original Image with Contours', frame)
    cv2.imshow('Gray Image', imgray)
    cv2.imshow('Thresholded Image', thresh)
    
    cv2.waitKey(0)  # Wait for a key press to close windows
    cv2.destroyAllWindows()

# Call the function with your image path and the desired output path
image_path = 'path_to_your_image.jpg'
output_path = 'path_to_save_result.jpg'
process_image(image_path, output_path)

