from PyQt5 import QtWidgets, QtCore
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from GRAFS import Grafs
from Correlation import  Grafs_GOLD

 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton.setGeometry( QtCore.QRect(10, 10, 200, 200))

 


 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

###################################################################################

def button():
	nka = application.ui.spinBox.value()
	data = application.ui.spinBox.value()
	t = application.ui.lineEdit.text()
	e = application.ui.lineEdit_2.text()
	i = application.ui.lineEdit_9.text()
	dqdt = application.ui.lineEdit_11.text()
	A = application.ui.lineEdit_3.text()
	L = application.ui.lineEdit_4.text()
	w = application.ui.lineEdit_5.text()
	m  = application.ui.lineEdit_6.text()
	af0 = application.ui.lineEdit_7.text()
	af1 = application.ui.lineEdit_8.text()


	Grafs(str(nka))

def button2():
	nka = application.ui.spinBox.value()
	Grafs_GOLD(str(nka))

		

application.ui.pushButton.clicked.connect(button)
application.ui.pushButton_2.clicked.connect(button2)




####################################################################################
sys.exit(app.exec())



