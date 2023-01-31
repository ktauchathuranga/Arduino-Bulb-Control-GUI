from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys
import serial

comPort = "COM"
arduinoBoard = ""
userComPort = ""

while True:
    try:
        userComPort = int(input("Enter Arduino COM Port Number (0,1,2,...) : "))
    except:
        print("Enter Valid Value!")
    if type(userComPort) == int:
        break


if int(userComPort) != "":
    comPort += str(userComPort)

print(comPort)
try:
    arduinoBoard = serial.Serial(comPort, 9600)

except:
    print('Arduino Board Connection Failed!')
    exit()

print(arduinoBoard.readline().decode('utf8'))

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load('bulb.ui', None)
window.textBrowser.setText('OFF')


def action(data):
    if data is True:
        arduinoBoard.write('1'.encode())
        window.textBrowser.setText('ON')
    else:
        arduinoBoard.write('0'.encode())
        window.textBrowser.setText('OFF')


window.pBotton.clicked.connect(action)

window.show()
app.exec()
