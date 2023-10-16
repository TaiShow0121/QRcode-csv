
import csv
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# QRコードをデコード

decoded_data = decode(Image.open('01.png'))[0].data.decode('utf-8')

# デコードしたデータを分割
surname, name, number, company = decoded_data.split(' ')

# CSVファイルに書き込む
csv_name = input()

with open(csv_name + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Surname', 'Name', 'Number', 'Company'])  # 一行目
    writer.writerow([surname, name, number, company])  # 二行目