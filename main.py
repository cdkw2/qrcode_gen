import qrcode

url = input("Enter the URL to generate QR code for: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

print(qr.terminal())
