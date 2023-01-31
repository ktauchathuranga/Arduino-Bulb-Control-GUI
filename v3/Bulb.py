from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys
import serial

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load('bulb.ui', None)
window.textBrowser.setText('OFF')


def disconnect():
    if window.pButton3.clicked:
        window.pButton2.clicked.connect(arduinoBoard.close())
        window.textBrowser2.setText("Port Disconnected")


def pinAction():
    global arduinoBoard
    port = str(window.spinBox.value())
    portDetail = "COM" + port
    try:
        arduinoBoard = serial.Serial(portDetail, 9600)

    except:
        window.textBrowser2.setText('Wrong Port or Board Not Connected')
        return
    ardRead = arduinoBoard.readline().decode().strip()
    window.textBrowser2.setText(ardRead)
    window.pButton3.clicked.connect(disconnect)

    def action(data):
        if arduinoBoard.isOpen():
            if data is True:
                arduinoBoard.write('1'.encode())
                window.textBrowser.setText('ON')
            else:
                arduinoBoard.write('0'.encode())
                window.textBrowser.setText('OFF')
        else:
            window.textBrowser2.setText("Port Not Opened")

    window.pBotton.clicked.connect(action)


window.pButton2.clicked.connect(pinAction)

window.show()
app.exec()
