import qrcode as qr

img = qr.make('https://www.youtube.com/watch?v=FOGRHBp6lvM')
img.save('wsCube.png')

