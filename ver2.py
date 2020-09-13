#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\drug coating\software\ver2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from all_ import *
from threads import *
import queue

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 480)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(20, 0, 706, 191))

		# self.widget.setGeometry(QtCore.QRect(0, 0, 800, 191))

		self.widget.setObjectName("widget")
		self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_13.setObjectName("horizontalLayout_13")

		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")

		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/arrows/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/arrows/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon.addPixmap(QtGui.QPixmap(":/up/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
###################################################################################
		self.spray_ob = spray_c(icon, icon1)
####################################################################################
		self.horizontalLayout_13.addLayout(self.spray_ob.horizontalLayout)
	
##########################################################################################
		self.dry_ob = dry_c(icon, icon1)
########################################################################################

		self.horizontalLayout_13.addLayout(self.dry_ob.horizontalLayout)
########################################################################################
		self.num_ob = n_cycle(icon, icon1)
		self.horizontalLayout_13.addLayout(self.num_ob.horizontalLayout)
####################################################################################
		
		font = QtGui.QFont()
		font.setPointSize(20)
		font1 = QtGui.QFont()
		font1.setPointSize(14)
		self.widget1 = QtWidgets.QWidget(self.centralwidget)
		self.widget1.setGeometry(QtCore.QRect(240, 220, 300, 200))
		self.widget1.setObjectName("widget1")

		self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_14.setObjectName("horizontalLayout_14")

		self.vertical_14 = QtWidgets.QVBoxLayout(self.widget1)
		self.vertical_14.setContentsMargins(0, 0, 0, 0)
		self.vertical_14.setObjectName("vertical_14")

		self.flow_rate_label = QtWidgets.QLabel()
		self.flow_rate_label.setObjectName("flow_rate_label")
		self.vertical_14.addWidget(self.flow_rate_label)
		self.flow_rate_label.setText("Current flow rate: 0 ml/min")
		self.flow_rate_label.setFont(font1)

		self.total_volume = QtWidgets.QLabel()
		self.total_volume.setObjectName("total_volume")
		self.vertical_14.addWidget(self.total_volume)
		self.total_volume.setText("Volume : 0 ml")
		self.total_volume.setFont(font1)
		
		self.label_2 = QtWidgets.QLabel()
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_14.addWidget(self.label_2)



		self.current = QtWidgets.QLabel(self.widget1)
		self.current.setObjectName("current")
		


		self.current_cycle = QtWidgets.QLCDNumber(self.widget1)
		self.current_cycle.setDigitCount(2)
		self.current_cycle.setObjectName("current_cycle")
		

		self.horizontalLayout_14.addWidget(self.current_cycle)
		self.vertical_14.addLayout(self.horizontalLayout_14)
		self.vertical_14.addWidget(self.current)
		
		self.widget2 = QtWidgets.QWidget(self.centralwidget)
		self.widget2.setGeometry(QtCore.QRect(580, 240, 220, 180))
		self.widget2.setObjectName("widget2")

		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.start = QtWidgets.QPushButton(self.widget2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
		self.start.setSizePolicy(sizePolicy)
		self.font = QtGui.QFont()
		self.font.setPointSize(20)
		self.start.setFont(self.font)
		self.start.setStyleSheet("background-color: rgb(172, 255, 127);")
		self.start.setObjectName("start")
		self.verticalLayout_4.addWidget(self.start)

		self.stop = QtWidgets.QPushButton(self.widget2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
		self.stop.setSizePolicy(sizePolicy)

		self.stop.setFont(self.font)
		self.stop.setStyleSheet("background-color: rgb(255, 85, 0);")
		self.stop.setObjectName("stop")
		self.verticalLayout_4.addWidget(self.stop)
		# self.spray.raise_()
		self.label_2.raise_()
		self.label_2.raise_()
		self.current_cycle.raise_()
		self.start.raise_()
		self.stop.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.newfont = QtGui.QFont("Times", 14)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.on_clicks()
		self.current_process = "Coating: "
		self.sprayer_with_pi = spraying_thread()
		self.sprayer_with_pi.cycle_done_signal.connect(self.update_cycles)
		self.sprayer_with_pi.dry_cycle.connect(self.running_drying_cycle)
		self.sprayer_with_pi.coating_cycle.connect(self.running_coating_cycle)
		self.sprayer_with_pi.timer_signal.connect(self.update_process)
		font1 = QtGui.QFont()
		font1.setPointSize(20)

		self.current.setFont(font1)
		self.sprayer_with_pi.completed.connect(self.completed)

##################################################################################################
		self.for_volume = volum_input()
		self.widget_vol = QtWidgets.QWidget(self.centralwidget)
		self.widget_vol.setGeometry(QtCore.QRect(20, 300, 200, 150))
		self.widget_vol.setObjectName("widget_vol")
		self.vertical_vol = QtWidgets.QGridLayout(self.widget_vol)
		# self.vertical_vol.addLayout(self.for_volume.verticalLayout)
		self.vertical_vol.addWidget(self.for_volume.volume_label,0,0,1,1)
		self.vertical_vol.addWidget(self.for_volume.horizontalSlider,1,0,1,1)
		self.vertical_vol.addWidget(self.for_volume.doubleSpinBox,2,0,1,1)

		self.for_volume.horizontalSlider.valueChanged['int'].connect(self.volume_display)
		self.q = queue.Queue(1)
		self.volume_q = queue.Queue()
		self.total_vol_q = queue.Queue(1)

		
		self.flow__ = flow_meter_readings(self.q, self.volume_q)
		# self.flow__.start()
		self.updating_thread = update_thread()
		self.updating_thread.start()

		self.updating_thread.updator_signal.connect(self.update_flow_rate)
		self.volume_calculating_thread = volume_calculating_thread(self.volume_q, self.total_vol_q)
		# self.volume_calculating_thread.start()

	def on_clicks(self):
		self.spray_ob.s_1_up.clicked.connect(self.s_1_up_clicked)
		self.spray_ob.s_2_up.clicked.connect(self.s_2_up_clicked)
		self.spray_ob.s_3_up.clicked.connect(self.s_3_up_clicked)
		self.spray_ob.s_1_down.clicked.connect(self.s_1_down_clicked)
		self.spray_ob.s_2_down.clicked.connect(self.s_2_down_clicked)
		self.spray_ob.s_3_down.clicked.connect(self.s_3_down_clicked)
		self.dry_ob.d_1_up.clicked.connect(self.d_1_up_clicked)
		self.dry_ob.d_2_up.clicked.connect(self.d_2_up_clicked)
		self.dry_ob.d_1_down.clicked.connect(self.d_1_down_clicked)
		self.dry_ob.d_2_down.clicked.connect(self.d_2_down_clicked)
		self.num_ob.n_1_up.clicked.connect(self.n_1_up_clicked)
		self.num_ob.n_2_up.clicked.connect(self.n_2_up_clicked)
		self.num_ob.n_1_down.clicked.connect(self.n_1_down_clicked)
		self.num_ob.n_2_down.clicked.connect(self.n_2_down_clicked)
		self.start.clicked.connect(self.start_process)
		self.stop.clicked.connect(self.stop_process)

	def up_check(self,current_val):
		if abs(current_val)>=0 and abs(current_val)<9:
			return True
		else:
			return False

	def down_check(self, current_val):
		if abs(current_val)>0 and abs(current_val)<=9:
			return True
		else:
			return False

	def s_1_up_clicked(self):
		if self.up_check(self.spray_ob.s1_val):
			self.spray_ob.s1_val +=1
			print("Clicked")
			self.spray_ob.s1.display(self.spray_ob.s1_val)
		pass
	
	def s_2_up_clicked(self):
		if self.up_check(self.spray_ob.s2_val):
			self.spray_ob.s2_val +=1
			self.spray_ob.s2.display(self.spray_ob.s2_val)
		pass

	def s_3_up_clicked(self):
		if self.up_check(self.spray_ob.s3_val):
			self.spray_ob.s3_val +=1
			self.spray_ob.s3.display(self.spray_ob.s3_val)
		pass
	def s_1_down_clicked(self):
		if self.down_check(self.spray_ob.s1_val):
			self.spray_ob.s1_val -=1
			self.spray_ob.s1.display(self.spray_ob.s1_val)
		pass
	def s_2_down_clicked(self):
		if self.down_check(self.spray_ob.s2_val):
			self.spray_ob.s2_val -=1
			self.spray_ob.s2.display(self.spray_ob.s2_val)
		pass
	def s_3_down_clicked(self):
		if self.down_check(self.spray_ob.s3_val):
			self.spray_ob.s3_val -=1
			self.spray_ob.s3.display(self.spray_ob.s3_val)
		pass
	def d_1_up_clicked(self):
		if self.up_check(self.dry_ob.d1_val):
			self.dry_ob.d1_val +=1
			self.dry_ob.d1.display(self.dry_ob.d1_val)
		pass
	def d_2_up_clicked(self):
		if self.up_check(self.dry_ob.d2_val):
			self.dry_ob.d2_val +=1
			self.dry_ob.d2.display(self.dry_ob.d2_val)
		pass
	def d_1_down_clicked(self):
		if self.down_check(self.dry_ob.d1_val):
			self.dry_ob.d1_val -=1
			self.dry_ob.d1.display(self.dry_ob.d1_val)
		pass
	def d_2_down_clicked(self):
		if self.down_check(self.dry_ob.d2_val):
			self.dry_ob.d2_val -=1
			self.dry_ob.d2.display(self.dry_ob.d2_val)
		pass
	def n_1_up_clicked(self):
		if self.up_check(self.num_ob.n1_val):
			self.num_ob.n1_val +=1
			self.num_ob.n1.display(self.num_ob.n1_val)
		pass
	def n_2_up_clicked(self):
		if self.up_check(self.num_ob.n2_val):
			self.num_ob.n2_val +=1
			self.num_ob.n2.display(self.num_ob.n2_val)
		pass
	def n_1_down_clicked(self):
		if self.down_check(self.num_ob.n1_val):
			self.num_ob.n1_val -=1
			self.num_ob.n1.display(self.num_ob.n1_val)
		pass
	def n_2_down_clicked(self):
		if self.down_check(self.num_ob.n2_val):
			self.num_ob.n2_val -=1
			self.num_ob.n2.display(self.num_ob.n2_val)
		pass
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# 		
		# self.number.setText(_translate("MainWindow", "No. of cycle:"))
		self.label_2.setText(_translate("MainWindow", "Currently running \n         cycle"))
		self.label_2.setFont(self.newfont)
		self.start.setText(_translate("MainWindow", "Start"))
		self.stop.setText(_translate("MainWindow", "Stop"))
		self.current.setText(_translate("MainWindow", "Stopped"))


	def start_process(self):
		spraying_time = int(self.spray_ob.find_value())
		drying_time = int(self.dry_ob.find_value())
		cycles = int(self.num_ob.find_value())
		print("Spraying for " + str(spraying_time)+" seconds")
		print("Drying for "+str(drying_time)+" seconds")
		print("Run for "+str(cycles)+" cycles")
		self.sprayer_with_pi.set_para(spraying_time, drying_time, cycles)
		self.sprayer_with_pi.start()
		# if self.for_volume.doubleSpinBox.value()!=0:
		self.volume_calculating_thread.set_zero()
		self.flow__.start_volume()
		# if self.for_volume.doubleSpinBox.value()!=0:


	def stop_process(self):
		self.sprayer_with_pi.stop()	
		self.current.setText("Stopped")	
		# self.volume_calculating_thread.set_zero()
		self.flow__.stop_volume()


	def update_cycles(self, val):
		self.current_cycle.display(val)


	def running_coating_cycle(self):
		_translate = QtCore.QCoreApplication.translate
		self.current_process = "Coating: "
		# self.current.setText(_translate("MainWindow", "Coating"))

	def running_drying_cycle(self):
		_translate = QtCore.QCoreApplication.translate
		self.current_process = "Drying: "
		# self.current.setText(_translate("MainWindow", "Dyring"))

	def update_process(self, ti):
		self.current.setText(self.current_process+str(ti))


	def completed(self):
		self.current.setText("Completed")
		self.flow__.stop_volume()

	def volume_display(self,val):
		self.for_volume.doubleSpinBox.setValue(val)

	def update_flow_rate(self):
		if self.q.full():
			f_val = self.q.get()
			self.flow_rate_label.setText("Current flow rate: "+str(f_val/1000)+" ml/min")
		if self.total_vol_q.full():
			self.t_v = round(self.total_vol_q.get(),2)     #################change
			self.total_volume.setText("volum: "+str(self.t_v)+" ml")
			if self.t_v >= self.for_volume.doubleSpinBox.value() and self.for_volume.doubleSpinBox.value()!=0:
				self.sprayer_with_pi.final_dry = True     ################### add
				self.stop_process()                         
				self.sprayer_with_pi.final_dry = False       ################# add
import arr_rc

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

