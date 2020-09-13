#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
import time
# import RPi.#GPIO as #GPIO

class spraying_thread(QtCore.QThread):
	cycle_done_signal = QtCore.pyqtSignal(int)
	def __init__(self):
		super(spraying_thread,self).__init__()
		self.m1_pin = 16
		self.m2_pin = 18
		self.m3_pin = 12 
		self.v1_pin = 15
		self.v2_pin = 11
		#GPIO.setmode(#GPIO.BOARD)
		# #GPIO.setwarnings(False)
		#GPIO.setup(self.m1_pin, #GPIO.OUT)
		#GPIO.setup(self.m2_pin, #GPIO.OUT)
		#GPIO.setup(self.m3_pin, #GPIO.OUT)
		#GPIO.setup(self.v1_pin, #GPIO.OUT)
		#GPIO.setup(self.v2_pin, #GPIO.OUT)

		#GPIO.output(self.m1_pin, #GPIO.LOW)
		#GPIO.output(self.m2_pin, #GPIO.LOW)
		#GPIO.output(self.m3_pin, #GPIO.LOW)
		#GPIO.output(self.v1_pin, #GPIO.LOW)
		#GPIO.output(self.v2_pin, #GPIO.LOW)
		self.shall_run = True
		
	def set_para(self, s_t, d_t, n_c):
		self.s_t = s_t
		self.d_t = d_t
		self.n_c = n_c
		self.shall_run = True

				
	def run(self):
		#GPIO.output(self.m1_pin, #GPIO.HIGH)
		#GPIO.output(self.m2_pin, #GPIO.HIGH)
		#GPIO.output(self.m3_pin, #GPIO.HIGH)
		#GPIO.output(self.v1_pin, #GPIO.HIGH)
		self.number = 1
		#GPIO.output(self.v2_pin, #GPIO.HIGH)
		self.v2_pin_status = True
		self.start_time = time.time()
		self.current = 0
		# self.cycle_done_signal.emit(self.number)
		while self.shall_run:
			if (time.time()-self.start_time)>=self.s_t and self.v2_pin_status:
				self.v2_pin_status = False
				#GPIO.output(self.v2_pin, #GPIO.LOW)
				self.start_time = time.time()
			if (time.time()-self.start_time)>=self.d_t and not self.v2_pin_status:
				self.v2_pin_status = True
				#GPIO.output(self.v2_pin, #GPIO.HIGH)
				self.number +=1
				self.start_time = time.time()
			if self.number > self.n_c:
				self.shall_run = False
			if self.number!=self.current:
				self.cycle_done_signal.emit(self.number)
				self.current = self.number	

	def stop(self):
		self.shall_run = False
		#GPIO.output(self.m1_pin, #GPIO.LOW)
		#GPIO.output(self.m2_pin, #GPIO.LOW)
		#GPIO.output(self.m3_pin, #GPIO.LOW)
		#GPIO.output(self.v1_pin, #GPIO.LOW)
		#GPIO.output(self.v2_pin, #GPIO.LOW)
		self.cycle_done_signal.emit(0)
		