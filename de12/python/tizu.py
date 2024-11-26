
import qrcode

# QRコードに変換したいURL
url = 'http://127.0.0.1:5500/digi_fab/re-za.html'  # ここに実際のURLを入力

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# 画像を作成
img = qr.make_image(fill_color="black", back_color="white")

# 画像を保存
img.save('qrcode.png')