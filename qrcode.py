import qrcode
import base64
import pandas as pd

file_path = "ENCODED_WORDS.xlsx"

df = pd.read_excel(file_path)
#read file
encoded_word = df.loc[1, 'encoded']

decoded = base64b64decode(encoded_word).decode()

qr = qrcode.QRCode(box_size=8, border=3)
#get ur own word
# qr.add_data(decoded_word)
#make qr and scan it
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
# img.show()
