from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Conta/Nova pasta/qrcodes para ler/myqrcode.png')

result = decode(img)

print(result)