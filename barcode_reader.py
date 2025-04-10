import cv2
from pyzbar.pyzbar import decode

def read_barcode(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Decode the barcode
    barcodes = decode(image)
    
    barcode_data = []
    
    for barcode in barcodes:
        # Extract the data from the barcode
        barcode_info = barcode.data.decode('utf-8')
        barcode_data.append(barcode_info)
        
        # Optionally, you can draw the bounding box around the barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the image with the barcode
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return barcode_data

# Example usage
barcode_info = read_barcode('/home/necro/Downloads/barcode_read.jpeg')
print('Decoded Barcode:', barcode_info)
