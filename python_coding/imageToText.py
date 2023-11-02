from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Path to the image file
image_path = 'IMG_1307.jpg'

# Open the image file
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
# print("Extracted Text:")
# print(text, len(text))
# print(text[text.index("INGREDIENTS"):], '------------------')
stripped_data = text[text.index("INGREDIENTS"):]
stripped_data = stripped_data.split('\n\n')
print(stripped_data[0], '------------------')


