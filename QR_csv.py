
import csv
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# QRコードをデコード
print("読み込むQRコード名:")
OpenQR = input()
decoded_data = decode(Image.open(OpenQR+'.png'))[0].data.decode('utf-8')

# デコードしたデータを分割
surname, name, number, company = decoded_data.split(' ')

# CSVファイルに書き込む
print("csv 名前を付けて保存:")
csv_name = input()

with open(csv_name + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Surname', 'Name', 'Number', 'Company'])  # 一行目
    writer.writerow([surname, name, number, company])  # 二行目
