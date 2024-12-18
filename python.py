import qrcode

# Data to br encoded in the QR code
data = "www.facebook.com "


# Create a QrCode instance
qr = qrcode.QRCode(
    version=1,   # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,   # Controls error correction level
    box_size=10,   # Size of each box (pixels)
    border=4,  # Size of the border (boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color='red', black_color='white')

# Save the image
img.save("qrcode_example.png")

# Display the image
img.show() 