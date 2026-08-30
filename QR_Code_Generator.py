import qrcode           # To Install - pip install qrcode

qr_data = input("Enter the Text or URL: ").strip()
img_name = input("Enter the Filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(qr_data)

img = qr.make_image(fill_color='black', back_color='white')
img.save(img_name)

print(f"QR Code saved as {img_name}")