import PySimpleGUI as sg
import qr_code


def qrcode_generierer(farbe):

    sg.theme(farbe)

    layout = [[sg.Text('Mein QRCode Generierer')], [sg.Input(key='-IN-')],
              [sg.Button('Erstellen'), sg.Exit()]]

    window = sg.Window('Window that stays open', layout)

    while True:                             # The Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Erstellen':
            qr_code.qrcode_erstellen(values['-IN-'], "site.png")
            sg.popup(f"Dein QRCode mit dem Text {values['-IN-']} wurde erstellt.")
    window.close()


def zeige_farben():
    sg.theme_previewer()


if __name__ == '__main__':
    #zeige_farben()
    qrcode_generierer("DarkTeal2")