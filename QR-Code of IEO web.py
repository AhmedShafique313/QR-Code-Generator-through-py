import qrcode


features = qrcode.QRCode(version=1, box_size=50, border=5)

features.add_data('ieo.is-great.org')
features.make(fit=True)
generate_image = features.make_image(fill_color="blue", back_color="white")
generate_image.save("IEO-WEB.png")
