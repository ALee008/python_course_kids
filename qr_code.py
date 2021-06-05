import qrcode


def qrcode_erstellen(text, dateiname):
    filename = "/Users/ali/PycharmProjects/qrcode_and_gui/output/" + dateiname
    img = qrcode.make(text)
    img.save(filename)


if __name__ == '__main__':
    qrcode_erstellen("BLABLA", "site.png")
