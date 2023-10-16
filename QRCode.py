import csv
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# QRコードを生成
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

print("姓:")
Surname = input()
print("名:")
name = input()
print("番号:")
Number = input()
print("会社名:")
Company = input()


qr.add_data((Surname +" "+ name +" "+ Number +" "+ Company).encode('utf-8'), optimize=0)
# qr.add_data("山田 太郎 123 株式会社ABC".encode('utf-8'), optimize=0)

qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
print("QRCode name:")
image_name = input()
img.save(image_name+".png")
