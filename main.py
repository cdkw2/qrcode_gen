import qrcode

url = input("Enter the URL to generate QR code for: ")

qr = qrcode.QRCode(version=1, box_size=1, border=4)
qr.add_data(url)
qr.make(fit=True)

matrix = qr.get_matrix()

for row in matrix:
    line = ""
    for col in row:
        if col:
            line += "  "
        else:
            line += "██"
    print(line)
