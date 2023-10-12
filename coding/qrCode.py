import qrcode, random
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import pyqrcode
import png
from pyqrcode import QRCode

qrcode_img=qrcode.make('2HTWKVM16QN2YD6JH1')
canvas=Image.new("RGB", (300,300),"white")
draw=ImageDraw.Draw(canvas)
canvas.paste(qrcode_img)
image_path = f"qrcode_{random.randint(1000,9999)}.png"
# buffer = BytesIO()
canvas.save(image_path, "PNG")
# canvas.save(buffer, "PNG")
canvas.close()
print(canvas,'done')