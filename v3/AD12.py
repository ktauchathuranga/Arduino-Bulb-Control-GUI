from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys
import serial

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load('AD12.ui', None)


def portNotOpened():
    window.textBrowserStatus.setText("Port Not Opened!")


def disconnect():
    if window.pButtonD.clicked:
        window.pButtonC.clicked.connect(arduinoBoard.close())
        window.textBrowserStatus.setText("Port Disconnected!")


def pinAction():
    global arduinoBoard
    port = str(window.spinBox.value())
    portDetail = "COM" + port
    try:
        arduinoBoard = serial.Serial(portDetail, 115200)

    except:
        window.textBrowserStatus.setText('Wrong Port or Board Not Connected!')
        return
    ardRead = arduinoBoard.readline().decode().strip()
    window.textBrowserStatus.setText(ardRead)
    window.pButtonD.clicked.connect(disconnect)

    def ardSigFunction(data):
        addingLine = data + "\n"
        arduinoBoard.write(addingLine.encode())

    def action2(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("2")
                window.textBrowser2.setText('ON')
            else:
                ardSigFunction("22")
                window.textBrowser2.setText('OFF')
        else:
            portNotOpened()

    def action3(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("3")
                window.textBrowser3.setText('ON')
            else:
                ardSigFunction("33")
                window.textBrowser3.setText('OFF')
        else:
            portNotOpened()

    def action4(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("4")
                window.textBrowser4.setText('ON')
            else:
                ardSigFunction("44")
                window.textBrowser4.setText('OFF')
        else:
            portNotOpened()

    def action5(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("5")
                window.textBrowser5.setText('ON')
            else:
                ardSigFunction("55")
                window.textBrowser5.setText('OFF')
        else:
            portNotOpened()

    def action6(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("6")
                window.textBrowser6.setText('ON')
            else:
                ardSigFunction("66")
                window.textBrowser6.setText('OFF')
        else:
            portNotOpened()

    def action7(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("7")
                window.textBrowser7.setText('ON')
            else:
                ardSigFunction("77")
                window.textBrowser7.setText('OFF')
        else:
            portNotOpened()

    def action8(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("8")
                window.textBrowser8.setText('ON')
            else:
                ardSigFunction("88")
                window.textBrowser8.setText('OFF')
        else:
            portNotOpened()

    def action9(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("9")
                window.textBrowser9.setText('ON')
            else:
                ardSigFunction("99")
                window.textBrowser9.setText('OFF')
        else:
            portNotOpened()

    def action10(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("10")
                window.textBrowser10.setText('ON')
            else:
                ardSigFunction("1010")
                window.textBrowser10.setText('OFF')
        else:
            portNotOpened()

    def action11(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("11")
                window.textBrowser11.setText('ON')
            else:
                ardSigFunction("1111")
                window.textBrowser11.setText('OFF')
        else:
            portNotOpened()

    def action12(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("12")
                window.textBrowser12.setText('ON')
            else:
                ardSigFunction("1212")
                window.textBrowser12.setText('OFF')
        else:
            portNotOpened()

    def action13(data):
        if arduinoBoard.isOpen():
            if data is True:
                ardSigFunction("13")
                window.textBrowser13.setText('ON')
            else:
                ardSigFunction("1313")
                window.textBrowser13.setText('OFF')
        else:
            portNotOpened()

    # window.pBotton0.clicked.connect(action0)
    # window.pBotton1.clicked.connect(action1)
    window.pBotton2.clicked.connect(action2)
    window.pBotton3.clicked.connect(action3)
    window.pBotton4.clicked.connect(action4)
    window.pBotton5.clicked.connect(action5)
    window.pBotton6.clicked.connect(action6)
    window.pBotton7.clicked.connect(action7)
    window.pBotton8.clicked.connect(action8)
    window.pBotton9.clicked.connect(action9)
    window.pBotton10.clicked.connect(action10)
    window.pBotton11.clicked.connect(action11)
    window.pBotton12.clicked.connect(action12)
    window.pBotton13.clicked.connect(action13)


window.pButtonC.clicked.connect(pinAction)

window.show()
app.exec()
