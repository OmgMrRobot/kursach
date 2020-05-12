from PyQt5 import QtWidgets, QtCore
from ux import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from GRAFS import CreateSpectrum
from KF import Graf_VKF
from Move_to_bits_ephemeris import Move_to_Bits_Ephemeris as MBE
import message213
from multiprocessing import Process

 
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
	PRN = application.ui.spinBox.value()
	graf = CreateSpectrum(str(PRN))
	graf.grafs()

def button2():
	PRN = application.ui.spinBox.value()
	PRN2 = application.ui.spinBox_2.value()

	Graf_VKF(str(PRN), str(PRN2))

def button3():
	PRN = application.ui.spinBox.value()

	Toe = application.ui.toe.text()

	e = application.ui.eccentricity.text()

	i = application.ui.orbital_iclinations.text()

	dqdt = application.ui.rate_of_right_ascen.text()

	A = application.ui.semi_major.text()

	right_ascen_at_week = application.ui.right_ascen_at_week.text()

	w = application.ui.perigree.text()

	m  = application.ui.anomaly.text()

	af0 = application.ui.af0.text()

	af1 = application.ui.af1.text()

	Cic = application.ui.cic.text()

	Cis = application.ui.cis.text()

	Crc = application.ui.crc.text()

	Crs = application.ui.crs.text()

	Cuc = application.ui.cuc.text()

	Cus = application.ui.cus.text()

	Tgd = application.ui.tgd.text()


	almanah = {"PRN" : PRN, "Toe" : Toe, "e" : e, "i" : i, "dqdt" : dqdt, 
	"A" : A, "right_ascen_at_week" : right_ascen_at_week, "w" : w, "m" : m, 
	"af0" : af0, "af1" : af1, "Cic" : Cic, "Cis" : Cis, "Crc" : Crc, "Crs" : Crs,
	"Cus" : Cus, "Cuc" : Cuc, "Tgd" : Tgd}



	for k,v in almanah.items():
		almanah[k] = float(v)
		print(f"{k} = {v}, {type(v)}\n")

	try:
		del message213.Message
		message213.Message = [] 
	except NameError:
		pass
	
	MBE(almanah)
	message213.Main_Message(almanah)

	with open('New_Message.txt', mode = 'w') as file:
		for i in message213.Message:
			file.write(str(i))

	# for k,v in almanah.items():
	# 	if not k == "PRN":
	# 		print(f"{k} = {v}, {len(v)}\n")


# 	print(f"PRN = {PRN}\n Toe = {Toe}\n eccentricity = {e}\n orbital_iclinations = {i}\n \
# rate_of_right_ascen = {dqdt}\n A = {A}\n right_ascen_at_week = {right_ascen_at_week}\n \
# w = {w}\n m = {m}")

application.ui.pushButton.clicked.connect(button2)
application.ui.pushButton_2.clicked.connect(button)
application.ui.pushButton_3.clicked.connect(button3)




####################################################################################
sys.exit(app.exec())



