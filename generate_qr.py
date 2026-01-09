import qrcode

# The secret flag
flag_data = "LNM{N07_H3R3}"

# Generate the QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(flag_data)
qr.make(fit=True)

# Save the file
img = qr.make_image(fill_color="black", back_color="white")
img.save("original.png")
print("Success: original.png has been created.")