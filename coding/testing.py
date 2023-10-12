import os
from PIL import Image

# source_dir = "/home/apptunix/Pictures/"
# output_dir = "./"

# for file in os.listdir(source_dir):
#     if file.split('.')[-1] == "jpg":
#         print(file, '-------------file---------------------')
#         image = Image.open(os.path.join(source_dir, file))
#         print(image, '------------image---------------')
#         image_converted = image.convert('RGB')
#         image_converted.save(os.path.join(output_dir, f"{file.split('.')[-2]}.pdf"))
#         print("converted")

all_attributes = os.getcwd()

print(all_attributes)