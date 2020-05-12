# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 1077)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: lightblue;")
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.Anomaly = QtWidgets.QLabel(self.widget)
        self.Anomaly.setStyleSheet("font-size: 24px;")
        self.Anomaly.setObjectName("Anomaly")
        self.gridLayout.addWidget(self.Anomaly, 0, 0, 1, 1)
        self.orbital_iclinations = QtWidgets.QLineEdit(self.widget)
        self.orbital_iclinations.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.orbital_iclinations.setObjectName("orbital_iclinations")
        self.gridLayout.addWidget(self.orbital_iclinations, 13, 0, 1, 1)
        self.eccentricity = QtWidgets.QLineEdit(self.widget)
        self.eccentricity.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.eccentricity.setObjectName("eccentricity")
        self.gridLayout.addWidget(self.eccentricity, 5, 0, 1, 1)
        self.Semi_major = QtWidgets.QLabel(self.widget)
        self.Semi_major.setStyleSheet("font-size: 24px;")
        self.Semi_major.setObjectName("Semi_major")
        self.gridLayout.addWidget(self.Semi_major, 8, 0, 1, 1)
        self.semi_major = QtWidgets.QLineEdit(self.widget)
        self.semi_major.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.semi_major.setObjectName("semi_major")
        self.gridLayout.addWidget(self.semi_major, 9, 0, 1, 1)
        self.Orbital_iclinations = QtWidgets.QLabel(self.widget)
        self.Orbital_iclinations.setStyleSheet("font-size: 24px;")
        self.Orbital_iclinations.setObjectName("Orbital_iclinations")
        self.gridLayout.addWidget(self.Orbital_iclinations, 12, 0, 1, 1)
        self.Right_ascen_at_week = QtWidgets.QLabel(self.widget)
        self.Right_ascen_at_week.setStyleSheet("font-size: 24px;")
        self.Right_ascen_at_week.setObjectName("Right_ascen_at_week")
        self.gridLayout.addWidget(self.Right_ascen_at_week, 10, 0, 1, 1)
        self.right_ascen_at_week = QtWidgets.QLineEdit(self.widget)
        self.right_ascen_at_week.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.right_ascen_at_week.setObjectName("right_ascen_at_week")
        self.gridLayout.addWidget(self.right_ascen_at_week, 11, 0, 1, 1)
        self.perigree = QtWidgets.QLineEdit(self.widget)
        self.perigree.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.perigree.setObjectName("perigree")
        self.gridLayout.addWidget(self.perigree, 15, 0, 1, 1)
        self.Rate_of_right_ascen = QtWidgets.QLabel(self.widget)
        self.Rate_of_right_ascen.setStyleSheet("font-size: 24px;")
        self.Rate_of_right_ascen.setObjectName("Rate_of_right_ascen")
        self.gridLayout.addWidget(self.Rate_of_right_ascen, 6, 0, 1, 1)
        self.Eccentricity = QtWidgets.QLabel(self.widget)
        self.Eccentricity.setStyleSheet("font-size: 24px;")
        self.Eccentricity.setObjectName("Eccentricity")
        self.gridLayout.addWidget(self.Eccentricity, 4, 0, 1, 1)
        self.anomaly = QtWidgets.QLineEdit(self.widget)
        self.anomaly.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.anomaly.setObjectName("anomaly")
        self.gridLayout.addWidget(self.anomaly, 1, 0, 1, 1)
        self.Perigree = QtWidgets.QLabel(self.widget)
        self.Perigree.setStyleSheet("font-size: 24px;")
        self.Perigree.setObjectName("Perigree")
        self.gridLayout.addWidget(self.Perigree, 14, 0, 1, 1)
        self.Toe = QtWidgets.QLabel(self.widget)
        self.Toe.setStyleSheet("font-size: 24px;")
        self.Toe.setObjectName("Toe")
        self.gridLayout.addWidget(self.Toe, 2, 0, 1, 1)
        self.toe = QtWidgets.QLineEdit(self.widget)
        self.toe.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.toe.setObjectName("toe")
        self.gridLayout.addWidget(self.toe, 3, 0, 1, 1)
        self.rate_of_right_ascen = QtWidgets.QLineEdit(self.widget)
        self.rate_of_right_ascen.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.rate_of_right_ascen.setObjectName("rate_of_right_ascen")
        self.gridLayout.addWidget(self.rate_of_right_ascen, 7, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.af1 = QtWidgets.QLineEdit(self.widget1)
        self.af1.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.af1.setObjectName("af1")
        self.gridLayout_2.addWidget(self.af1, 3, 0, 1, 1)
        self.Cuc = QtWidgets.QLabel(self.widget1)
        self.Cuc.setStyleSheet("font-size: 24px;")
        self.Cuc.setObjectName("Cuc")
        self.gridLayout_2.addWidget(self.Cuc, 12, 0, 1, 1)
        self.cis = QtWidgets.QLineEdit(self.widget1)
        self.cis.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.cis.setObjectName("cis")
        self.gridLayout_2.addWidget(self.cis, 11, 0, 1, 1)
        self.Cic = QtWidgets.QLabel(self.widget1)
        self.Cic.setStyleSheet("font-size: 24px;")
        self.Cic.setObjectName("Cic")
        self.gridLayout_2.addWidget(self.Cic, 8, 0, 1, 1)
        self.Cus = QtWidgets.QLabel(self.widget1)
        self.Cus.setStyleSheet("font-size: 24px;")
        self.Cus.setObjectName("Cus")
        self.gridLayout_2.addWidget(self.Cus, 14, 0, 1, 1)
        self.crc = QtWidgets.QLineEdit(self.widget1)
        self.crc.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.crc.setObjectName("crc")
        self.gridLayout_2.addWidget(self.crc, 22, 0, 1, 1)
        self.cuc = QtWidgets.QLineEdit(self.widget1)
        self.cuc.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.cuc.setObjectName("cuc")
        self.gridLayout_2.addWidget(self.cuc, 13, 0, 1, 1)
        self.cic = QtWidgets.QLineEdit(self.widget1)
        self.cic.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.cic.setObjectName("cic")
        self.gridLayout_2.addWidget(self.cic, 9, 0, 1, 1)
        self.Crs = QtWidgets.QLabel(self.widget1)
        self.Crs.setStyleSheet("font-size: 24px;")
        self.Crs.setObjectName("Crs")
        self.gridLayout_2.addWidget(self.Crs, 23, 0, 1, 1)
        self.Af0 = QtWidgets.QLabel(self.widget1)
        self.Af0.setStyleSheet("font-size: 24px;")
        self.Af0.setObjectName("Af0")
        self.gridLayout_2.addWidget(self.Af0, 0, 0, 1, 1)
        self.cus = QtWidgets.QLineEdit(self.widget1)
        self.cus.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.cus.setObjectName("cus")
        self.gridLayout_2.addWidget(self.cus, 15, 0, 1, 1)
        self.Tgd = QtWidgets.QLabel(self.widget1)
        self.Tgd.setStyleSheet("font-size: 24px;")
        self.Tgd.setObjectName("Tgd")
        self.gridLayout_2.addWidget(self.Tgd, 25, 0, 1, 1)
        self.af0 = QtWidgets.QLineEdit(self.widget1)
        self.af0.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.af0.setObjectName("af0")
        self.gridLayout_2.addWidget(self.af0, 1, 0, 1, 1)
        self.Crc = QtWidgets.QLabel(self.widget1)
        self.Crc.setStyleSheet("font-size: 24px;")
        self.Crc.setObjectName("Crc")
        self.gridLayout_2.addWidget(self.Crc, 21, 0, 1, 1)
        self.tgd = QtWidgets.QLineEdit(self.widget1)
        self.tgd.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.tgd.setObjectName("tgd")
        self.gridLayout_2.addWidget(self.tgd, 26, 0, 1, 1)
        self.crs = QtWidgets.QLineEdit(self.widget1)
        self.crs.setStyleSheet("background-color: white;\n"
"height: 40px;\n"
"font-size: 25px;\n"
"")
        self.crs.setObjectName("crs")
        self.gridLayout_2.addWidget(self.crs, 24, 0, 1, 1)
        self.Af1 = QtWidgets.QLabel(self.widget1)
        self.Af1.setStyleSheet("font-size: 24px;")
        self.Af1.setObjectName("Af1")
        self.gridLayout_2.addWidget(self.Af1, 2, 0, 1, 1)
        self.Cis = QtWidgets.QLabel(self.widget1)
        self.Cis.setStyleSheet("font-size: 24px;")
        self.Cis.setObjectName("Cis")
        self.gridLayout_2.addWidget(self.Cis, 10, 0, 1, 1)
        self.tabWidget.addTab(self.widget1, "")
        self.gridLayout_3.addWidget(self.tabWidget, 3, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("height: 35px;\n"
"font-size: 20px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("height: 35px;\n"
"font-size: 20px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("height: 35px;\n"
"font-size: 20px;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.PRN = QtWidgets.QLabel(self.centralwidget)
        self.PRN.setStyleSheet("font-size: 30px;\n"
"background-color: lightgreen;\n"
"\n"
"")
        self.PRN.setObjectName("PRN")
        self.gridLayout_3.addWidget(self.PRN, 0, 0, 1, 3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setBaseSize(QtCore.QSize(100, 100))
        self.spinBox.setStyleSheet("height: 40px;\n"
"font-size: 25px;\n"
"")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(32)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 1, 0, 1, 3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setStyleSheet("height: 40px;\n"
"font-size: 25px;\n"
"")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Альманах</p></body></html>"))
        self.Anomaly.setText(_translate("MainWindow", "<html><head/><body><p>m - средняя аномалия (mean anomaly)</p></body></html>"))
        self.orbital_iclinations.setText(_translate("MainWindow", "0.978742"))
        self.eccentricity.setText(_translate("MainWindow", "0.009441"))
        self.Semi_major.setText(_translate("MainWindow", "A - главная полуось ( semi-major axis)"))
        self.semi_major.setText(_translate("MainWindow", "5153.584"))
        self.Orbital_iclinations.setText(_translate("MainWindow", "i - угол наклонениiя (Orbital inclinations)"))
        self.Right_ascen_at_week.setText(_translate("MainWindow", "<html><head/><body><p>Ω<span style=\" font-size:6pt;\">0 </span><span style=\" font-size:14pt;\"> - </span>долгота восходящего узла орбитальной плоскости (right ascen at weel (rad))</p></body></html>"))
        self.right_ascen_at_week.setText(_translate("MainWindow", "-1.58222"))
        self.perigree.setText(_translate("MainWindow", "0.754676"))
        self.Rate_of_right_ascen.setText(_translate("MainWindow", "dΩ/dt скорость изменения восходящего узла орбиты (rate of  right ascen rad/s )"))
        self.Eccentricity.setText(_translate("MainWindow", "e - эксцентриситет (eccentricity)"))
        self.anomaly.setText(_translate("MainWindow", "3.029645"))
        self.Perigree.setText(_translate("MainWindow", " ω - аргумент перигея (argument of perigee)"))
        self.Toe.setText(_translate("MainWindow", "<html><head/><body><p>t - опорное время привязки эфемерид (reference time ephemeris)</p></body></html>"))
        self.toe.setText(_translate("MainWindow", "405504000.000000"))
        self.rate_of_right_ascen.setText(_translate("MainWindow", "7.874614e-12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Альманах"))
        self.af1.setText(_translate("MainWindow", "-1.091394e-11"))
        self.Cuc.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" font-size:10pt;\">uc </span>- косинусная поправка аргумента долготы</p></body></html>"))
        self.cis.setText(_translate("MainWindow", "3.352761e-08"))
        self.Cic.setText(_translate("MainWindow", "<html><head/><body><p> C<span style=\" font-size:10pt;\">ic</span> - косинусная поправка к углу наклонения</p></body></html>"))
        self.Cus.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" font-size:10pt;\">us</span> - синусная поправка аргумента долготы</p></body></html>"))
        self.crc.setText(_translate("MainWindow", "228.250000"))
        self.cuc.setText(_translate("MainWindow", "-2.689660e-06"))
        self.cic.setText(_translate("MainWindow", "-1.713634e-07"))
        self.Crs.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" font-size:10pt;\">rs -</span> cинусная поправка радиуса орбиты</p></body></html>"))
        self.Af0.setText(_translate("MainWindow", "Af0(s)"))
        self.cus.setText(_translate("MainWindow", "8.463860e-06"))
        self.Tgd.setText(_translate("MainWindow", "<html><head/><body><p>t<span style=\" font-size:10pt;\">gd</span> - оценка групповой дифференциальной задержки</p></body></html>"))
        self.af0.setText(_translate("MainWindow", "-3.089905e-01"))
        self.Crc.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" font-size:10pt;\">rc </span>- косинусная поправка радиуса орбиты</p></body></html>"))
        self.tgd.setText(_translate("MainWindow", "-1.257285e-05"))
        self.crs.setText(_translate("MainWindow", "-49.781250"))
        self.Af1.setText(_translate("MainWindow", "Af1(s)"))
        self.Cis.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" font-size:10pt;\">is</span> - синусная поправка к углу наклонения</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget1), _translate("MainWindow", "Поправки"))
        self.pushButton.setText(_translate("MainWindow", "AKF and VKF"))
        self.pushButton_2.setText(_translate("MainWindow", "Spectrum"))
        self.pushButton_3.setText(_translate("MainWindow", "Create Navigation Message"))
        self.PRN.setText(_translate("MainWindow", "PRN - номер НКА"))
