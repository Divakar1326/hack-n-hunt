import qrcode
import base64
import pandas as pd

# Location of your Excel file
file_path = r"C:/Users/diva1/OneDrive/Desktop/Hack'n Hunt/ENCODED WORDS.xlsx"

# Load Excel file
df = pd.read_excel(file_path)

# Get the first encoded word (row 0, column 'encoded_secret')
encoded_secret = df.loc[1, 'encoded']

# Decode the word
secret_word = base64.b64decode(encoded_secret).decode("utf-8")

# Create QR code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(secret_word)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Show and save
img.show()

