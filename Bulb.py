from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys
import serial

aa = serial.Serial('COM3', 9600)
print(aa.readline().decode('utf8'))

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load('bulb.ui', None)
window.setWindowTitle('Bulb')


def action(data):
    if data is True:
        aa.write('1'.encode())
        window.textBrowser.setText('ON')
    else:
        aa.write('0'.encode())
        window.textBrowser.setText('OFF')


window.pBotton.clicked.connect(action)

window.show()
app.exec()
