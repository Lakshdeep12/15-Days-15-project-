from PIL import Image
import qrcode as qr

qr = qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10, border=5)
qr.add_data('https://www.youtube.com/watch?v=FOGRHBp6lvM')
qr.make(fit=True)
qr.make_image(fill_color='red', back_color='white').save('wsCubeVideo.png')