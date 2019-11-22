from PyQt5 import QtWidgets, QtCore
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from GRAFS import Grafs
from GOLD_2 import Gold

 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton.setGeometry( QtCore.QRect(10, 10, 200, 200))

 


 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

#################################

def ab():
	nka = application.ui.spinBox.value()
	a = Gold(str(nka))
	print(a)
	# Grafs(str(nka))
	 


# nka = application.ui.spinBox.value()
# print(nka)


application.ui.pushButton_2.clicked.connect(ab)






###############################################
sys.exit(app.exec())


# nka = application.ui.spinBox.value()

# application.ui.pushButton.clicked.connect()


