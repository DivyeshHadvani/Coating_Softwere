#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets

class spray_c(QtWidgets.QWidget):
	def __init__(self, icon, icon1):
		super(spray_c, self).__init__()
		self.s1_val = 0
		self.s2_val = 0
		self.s3_val = 0
		#######################################################
		self.s_3_up = QtWidgets.QPushButton()
		self.s_3_up.setText("")
		self.s_3_up.setIcon(icon)
		self.s_3_up.setIconSize(QtCore.QSize(50, 50))
		self.s_3_up.setObjectName("s_3_up")
		######################################################
		self.s_2_up = QtWidgets.QPushButton()
		self.s_2_up.setText("")
		self.s_2_up.setIcon(icon)
		self.s_2_up.setIconSize(QtCore.QSize(50, 50))
		self.s_2_up.setObjectName("s_2_up")
		#####################################################
		self.s_1_up = QtWidgets.QPushButton()
		self.s_1_up.setText("")
		self.s_1_up.setIcon(icon)
		self.s_1_up.setIconSize(QtCore.QSize(50, 50))
		self.s_1_up.setObjectName("s_1_up")
		######################################################
		#######################################################
		self.horizontalLayout_up = QtWidgets.QHBoxLayout()
		self.horizontalLayout_up.setObjectName("horizontalLayout_up")
		self.horizontalLayout_up.addWidget(self.s_3_up)
		self.horizontalLayout_up.addWidget(self.s_2_up)
		self.horizontalLayout_up.addWidget(self.s_1_up)
		####################################################
		####################################################
		self.s_3_down = QtWidgets.QPushButton()
		self.s_3_down.setText("")
		self.s_3_down.setIcon(icon1)
		self.s_3_down.setIconSize(QtCore.QSize(50, 50))
		self.s_3_down.setObjectName("s_3_down")
		###########################################
		self.s_2_down = QtWidgets.QPushButton()
		self.s_2_down.setText("")
		self.s_2_down.setIcon(icon1)
		self.s_2_down.setIconSize(QtCore.QSize(50, 50))
		self.s_2_down.setObjectName("s_2_down")
		#############################################
		self.s_1_down = QtWidgets.QPushButton()
		self.s_1_down.setText("")
		self.s_1_down.setIcon(icon1)
		self.s_1_down.setIconSize(QtCore.QSize(50, 50))
		self.s_1_down.setObjectName("s_1_down")
		###########################################################
		############################################################
		self.horizontalLayout_down = QtWidgets.QHBoxLayout()
		self.horizontalLayout_down.setObjectName("horizontalLayout_down")
		self.horizontalLayout_down.addWidget(self.s_3_down)
		self.horizontalLayout_down.addWidget(self.s_2_down)
		self.horizontalLayout_down.addWidget(self.s_1_down)
		#############################################################
		#############################################################

		#############################################################
		self.s3 = QtWidgets.QLCDNumber()
		self.s3.setDigitCount(1)
		self.s3.setObjectName("s3")
		self.s2 = QtWidgets.QLCDNumber()
		self.s2.setDigitCount(1)
		self.s2.setObjectName("s2")
		self.s1 = QtWidgets.QLCDNumber()
		self.s1.setDigitCount(1)
		self.s1.setObjectName("s1")
		###############################################################
		self.horizontalLayout_lcd = QtWidgets.QHBoxLayout()
		self.horizontalLayout_lcd.setObjectName("horizontalLayout_lcd")
		self.horizontalLayout_lcd.addWidget(self.s3)
		self.horizontalLayout_lcd.addWidget(self.s2)
		self.horizontalLayout_lcd.addWidget(self.s1)
		###############################################################
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.verticalLayout.addLayout(self.horizontalLayout_up)
		self.verticalLayout.addLayout(self.horizontalLayout_lcd)
		self.verticalLayout.addLayout(self.horizontalLayout_down)
		################################################################
		self.spray = QtWidgets.QLabel()
		self.spray.setObjectName("spray")
		newfont = QtGui.QFont("Times", 14)
		self.spray.setText("  Spray\n  cycle:\n   (in\nseconds)")
		self.spray.setFont(newfont)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout.addWidget(self.spray)
		self.horizontalLayout.addLayout(self.verticalLayout)

	def find_value(self):
		val = self.s3_val*100 + self.s2_val*10 + self.s1_val
		return val

class dry_c(QtWidgets.QWidget):
	def __init__(self,icon, icon1):
		super(dry_c, self).__init__()
		self.d1_val = 0
		self.d2_val = 0
		##############################################################
		##############################################################
		self.d_1_up = QtWidgets.QPushButton()
		self.d_1_up.setText("")
		self.d_1_up.setIcon(icon)
		self.d_1_up.setIconSize(QtCore.QSize(50, 50))
		self.d_1_up.setObjectName("d_1_up")
		##############################################################
		self.d_2_up = QtWidgets.QPushButton()	
		self.d_2_up.setText("")
		self.d_2_up.setIcon(icon)
		self.d_2_up.setIconSize(QtCore.QSize(50, 50))
		self.d_2_up.setObjectName("d_2_up")
		##############################################################
		self.horizontalLayout_up = QtWidgets.QHBoxLayout()
		self.horizontalLayout_up.setObjectName("horizontalLayout_up")
		self.horizontalLayout_up.addWidget(self.d_1_up)
		self.horizontalLayout_up.addWidget(self.d_2_up)
		###########################################################
		self.d_2_down = QtWidgets.QPushButton()
		self.d_2_down.setText("")
		self.d_2_down.setIcon(icon1)
		self.d_2_down.setIconSize(QtCore.QSize(50, 50))
		self.d_2_down.setObjectName("d_2_down")
		###############################################################
		self.d_1_down = QtWidgets.QPushButton()
		self.d_1_down.setText("")
		self.d_1_down.setIcon(icon1)
		self.d_1_down.setIconSize(QtCore.QSize(50, 50))
		self.d_1_down.setObjectName("d_1_down")
		###############################################################
		self.horizontalLayout_down = QtWidgets.QHBoxLayout()
		self.horizontalLayout_down.setObjectName("horizontalLayout_down")
		self.horizontalLayout_down.addWidget(self.d_1_down)
		self.horizontalLayout_down.addWidget(self.d_2_down)
		################################################

		#########################
		self.d2 = QtWidgets.QLCDNumber()
		self.d2.setDigitCount(1)
		self.d2.setObjectName("d2")
		#########################
		#########################
		self.d1 = QtWidgets.QLCDNumber()
		self.d1.setDigitCount(1)
		self.d1.setObjectName("d1")
		##########################
		self.horizontalLayout_lcd = QtWidgets.QHBoxLayout()
		self.horizontalLayout_lcd.setObjectName("horizontalLayout_lcd")
		self.horizontalLayout_lcd.addWidget(self.d1)
		self.horizontalLayout_lcd.addWidget(self.d2)
		##########################
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.verticalLayout.addLayout(self.horizontalLayout_up)
		self.verticalLayout.addLayout(self.horizontalLayout_lcd)
		self.verticalLayout.addLayout(self.horizontalLayout_down)
		#############################################################
		self.dry = QtWidgets.QLabel()
		self.dry.setObjectName("dry")
		newfont = QtGui.QFont("Times", 14)
		self.dry.setText("   Dry\n  cycle  :\n    (in\nseconds)")
		self.dry.setFont(newfont)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout.addWidget(self.dry)
		self.horizontalLayout.addLayout(self.verticalLayout)
		############################################################

	def find_value(self):
		val = self.d1_val*10 + self.d2_val
		return val

class n_cycle(QtWidgets.QWidget):
	def __init__(self,icon, icon1):
		super(n_cycle, self).__init__()
		self.n1_val = 0
		self.n2_val = 0
		##############################################################
		##############################################################
		self.n_1_up = QtWidgets.QPushButton()
		self.n_1_up.setText("")
		self.n_1_up.setIcon(icon)
		self.n_1_up.setIconSize(QtCore.QSize(50, 50))
		self.n_1_up.setObjectName("n_1_up")
		##############################################################
		self.n_2_up = QtWidgets.QPushButton()	
		self.n_2_up.setText("")
		self.n_2_up.setIcon(icon)
		self.n_2_up.setIconSize(QtCore.QSize(50, 50))
		self.n_2_up.setObjectName("n_2_up")
		##############################################################
		self.horizontalLayout_up = QtWidgets.QHBoxLayout()
		self.horizontalLayout_up.setObjectName("horizontalLayout_up")
		self.horizontalLayout_up.addWidget(self.n_2_up)
		self.horizontalLayout_up.addWidget(self.n_1_up)
		###########################################################
		self.n_2_down = QtWidgets.QPushButton()
		self.n_2_down.setText("")
		self.n_2_down.setIcon(icon1)
		self.n_2_down.setIconSize(QtCore.QSize(50, 50))
		self.n_2_down.setObjectName("n_2_down")
		###############################################################
		self.n_1_down = QtWidgets.QPushButton()
		self.n_1_down.setText("")
		self.n_1_down.setIcon(icon1)
		self.n_1_down.setIconSize(QtCore.QSize(50, 50))
		self.n_1_down.setObjectName("n_1_down")
		###############################################################
		self.horizontalLayout_down = QtWidgets.QHBoxLayout()
		self.horizontalLayout_down.setObjectName("horizontalLayout_down")
		self.horizontalLayout_down.addWidget(self.n_2_down)
		self.horizontalLayout_down.addWidget(self.n_1_down)
		################################################

		#########################
		self.n2 = QtWidgets.QLCDNumber()
		self.n2.setDigitCount(1)
		self.n2.setObjectName("n2")
		#########################
		#########################
		self.n1 = QtWidgets.QLCDNumber()
		self.n1.setDigitCount(1)
		self.n1.setObjectName("n1")
		##########################
		self.horizontalLayout_lcd = QtWidgets.QHBoxLayout()
		self.horizontalLayout_lcd.setObjectName("horizontalLayout_lcd")
		self.horizontalLayout_lcd.addWidget(self.n2)
		self.horizontalLayout_lcd.addWidget(self.n1)
		##########################
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.verticalLayout.addLayout(self.horizontalLayout_up)
		self.verticalLayout.addLayout(self.horizontalLayout_lcd)
		self.verticalLayout.addLayout(self.horizontalLayout_down)
		#############################################################
		self.number = QtWidgets.QLabel()
		self.number.setObjectName("number")
		newfont = QtGui.QFont("Times", 14)
		self.number.setText("Number\n    of      : \n cycles")
		self.number.setFont(newfont)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout.addWidget(self.number)
		self.horizontalLayout.addLayout(self.verticalLayout)
		############################################################

	def find_value(self):
		val = self.n2_val*10 + self.n1_val
		return val


class gpio_buttons(QtWidgets.QWidget):
	"""docstring for gpio_buttons"""
	def __init__(self):
		super(gpio_buttons, self).__init__()
		