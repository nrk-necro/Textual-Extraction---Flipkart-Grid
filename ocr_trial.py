import cv2
import matplotlib.pyplot as plt
import easyocr

# Load the image
IMAGE_PATH = '71YKYVMfVKL._AC_UF1000,1000_QL80_.jpg'
reader = easyocr.Reader(['en'])

# Get the OCR result
result = reader.readtext(IMAGE_PATH)

# List to store text with confidence > 90%
high_confidence_texts = []

# Filter results based on confidence score > 90%
for detection in result:
    bbox, text, confidence = detection

    if confidence > 0.90:  # Only keep results with more than 90% confidence
        high_confidence_texts.append((bbox, text, confidence))

# Print the filtered results
print("Filtered Results (Confidence > 90%):", high_confidence_texts)

# Optionally, you can display the filtered results on the image
img = cv2.imread(IMAGE_PATH)
font = cv2.FONT_HERSHEY_SIMPLEX
spacer = 100

# Drawing the high-confidence results onto the image
for bbox, text, confidence in high_confidence_texts:
    # You can extract specific coordinates if you want to use the bounding box
    top_left = tuple(bbox[0])

    # Add text to the image
    img = cv2.putText(img, text, (20, spacer), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    spacer += 30

# Display the image with filtered text
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Print the extracted high-confidence texts only
print([text for _, text, _ in high_confidence_texts])
