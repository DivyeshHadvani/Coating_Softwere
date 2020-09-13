#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
import time
# import RPi.GPIO as GPIO
import serial
import serial.tools.list_ports
class spraying_thread(QtCore.QThread):
	cycle_done_signal = QtCore.pyqtSignal(int)
	dry_cycle = QtCore.pyqtSignal()
	coating_cycle = QtCore.pyqtSignal()
	timer_signal = QtCore.pyqtSignal(int)
	completed = QtCore.pyqtSignal()
	def __init__(self):
		super(spraying_thread,self).__init__()
		self.m1_pin = 16
		self.m2_pin = 18
		self.m3_pin = 12 
		self.v1_pin = 11
		self.v2_pin = 15
		# GPIO.setmode(GPIO.BOARD)
		# GPIO.setwarnings(False)
		# GPIO.setup(self.m1_pin, GPIO.OUT)
		# GPIO.setup(self.m2_pin, GPIO.OUT)
		# GPIO.setup(self.m3_pin, GPIO.OUT)
		# GPIO.setup(self.v1_pin, GPIO.OUT)
		# GPIO.setup(self.v2_pin, GPIO.OUT)

		# GPIO.output(self.m1_pin, GPIO.LOW)
		# GPIO.output(self.m2_pin, GPIO.LOW)
		# GPIO.output(self.m3_pin, GPIO.LOW)
		# GPIO.output(self.v1_pin, GPIO.LOW)
		# GPIO.output(self.v2_pin, GPIO.LOW)
		self.final_dry = False   ######## add this
		self.shall_run = True
		
	def set_para(self, s_t=0, d_t=0, n_c=0):
		self.s_t = s_t
		self.d_t = d_t
		self.n_c = n_c
		self.shall_run = True
		# runner = []
		# for i in range(self.n_c):
		# 	runner.append(self.s_t)
		# 	runner.append(self.d_t)

	def dry_cycle_(self):
		# GPIO.output(self.v1_pin, GPIO.HIGH)	
		time.sleep(self.d_t)	
		# GPIO.output(self.v1_pin, GPIO.LOW)		
	def run(self):
		# GPIO.output(self.m1_pin, GPIO.HIGH)
		# GPIO.output(self.m2_pin, GPIO.HIGH)
		# GPIO.output(self.m3_pin, GPIO.HIGH)
		# GPIO.output(self.v1_pin, GPIO.HIGH)
		self.number = 1
		self.current = 0
		# GPIO.output(self.v2_pin, GPIO.HIGH)
		self.v2_pin_status = True
		self.start_time = time.time()
		print("Going in loop")
		# self.cycle_done_signal.emit(self.number)
		kl = 1
		self.temp_time = time.time()
		while self.shall_run:
			if (time.time()-self.start_time)>=self.s_t and self.v2_pin_status:
				self.dry_cycle.emit()
				self.v2_pin_status = False
				# GPIO.output(self.v2_pin, GPIO.LOW)
				self.start_time = time.time()
				self.temp_time = self.start_time
				kl=1
				self.timer_signal.emit(kl)
			if (time.time()-self.start_time)>=self.d_t and not self.v2_pin_status:
				self.v2_pin_status = True
				self.coating_cycle.emit()
				# GPIO.output(self.v2_pin, GPIO.HIGH)
				self.number +=1
				self.start_time = time.time()
				self.temp_time = self.start_time
				kl=1
				self.timer_signal.emit(kl)
			if self.number > self.n_c:
				self.stop()		
				self.shall_run = False
			
				break
			if self.number!=self.current:
				self.cycle_done_signal.emit(self.number)
				print(str(self.number)+" cycles")
				self.current = self.number
			if time.time()-self.temp_time >= 1:
				self.timer_signal.emit(kl)
				kl = kl + 1
				self.temp_time = time.time()
######################################## add this
		if self.final_dry:
			# GPIO.output(self.v1_pin, GPIO.HIGH)	
			time.sleep(self.d_t)	
			# GPIO.output(self.v1_pin, GPIO.LOW)
#########################################
		print("Coming out from loop")	


	def stop(self):
		print("Stop was called")
		# GPIO.output(self.m1_pin, GPIO.LOW)
		# GPIO.output(self.m2_pin, GPIO.LOW)
		# GPIO.output(self.m3_pin, GPIO.LOW)
		# GPIO.output(self.v1_pin, GPIO.LOW)
		# GPIO.output(self.v2_pin, GPIO.LOW)
		self.cycle_done_signal.emit(0)
		self.completed.emit()
		self.shall_run = False	




class flow_meter_readings(QtCore.QThread):
	flow_reading_signal = QtCore.pyqtSignal(float)

	def __init__(self,reading_q, volume_q):
		super(flow_meter_readings,self).__init__()
		self.reading_q = reading_q
		self.volume_q = volume_q

	def find_com(self):
		comlist = serial.tools.list_ports.comports()
		connected = []
		for element in comlist:
			if element.manufacturer == 'FTDI':
				com = element.device
				print(com)
		return com

	def run(self):
		print("I will find com first")
		self.com = self.find_com()
		self.connnected_successfully = False
		self.decimals = 1
		self.find_vol = False
		try:
			self.ser = serial.Serial(self.com,115200)
			self.connnected_successfully = True
		except:
			print("Could't connect flow meter")

		if self.connnected_successfully:
			try:
				self.ser.write(b'mru state.flow_data[0].scale.decimals\r\n')                     ### To know decimal points of reading
				time.sleep(0.1)
				print("Sent")
				self.reading__ = self.ser.read(self.ser.in_waiting)
				print(self.reading__)
				self.decimals = int(self.reading__.decode("utf-8")[:-3])
			except:
				print("Couldn't get the decimal reading... So taking default value as 1")
		self.read_successfully = True	
		temp_reading = 0
		self.start_time = time.time()
		if self.connnected_successfully:
			while True:
				try:
					self.ser.write(b'mri state.flow_data[0].filter[1].output\r\n')       ##### Sent to flow meter to ask for current reading
					self.start_time = time.time()
				except:
					print("Error")
				time.sleep(0.1)
				if self.ser.in_waiting>0:
					temp_reading = self.ser.read(self.ser.in_waiting)                           ##### Reading from buffer
					temp_reading = (int(temp_reading.decode("utf-8")[:-3]))/(10**self.decimals)       #####converting reading into float value
					if self.find_vol:
						cc = temp_reading*(time.time()-self.start_time)/60
						self.volume_q.put(cc)
						# print("volume: "+str(cc))
						# print(str(temp_reading) + "  " + str(time.time()-self.start_time))
				if self.reading_q.empty():
					self.reading_q.put(temp_reading)					
				else:
					previous = self.reading_q.get()
					self.reading_q.put(temp_reading)

	def start_volume(self):
		self.find_vol = True

	def stop_volume(self):
		self.find_vol = False

class update_thread(QtCore.QThread):
	updator_signal = QtCore.pyqtSignal()
	def __init__(self):
		super(update_thread,self).__init__()

	def run(self):
		self.shall__ = True
		while self.shall__:
			self.updator_signal.emit()
			time.sleep(0.2)

	def stop(self):
		self.shall__ = False


class volume_calculating_thread(QtCore.QThread):
	def __init__(self, volume_q, total_volume_q):
		super(volume_calculating_thread,self).__init__()
		self.total_volume = 0
		self.volume_q = volume_q
		self.find_vol = True
		self.total_volume_q = total_volume_q

	def run(self):
		while self.find_vol:
			# print(self.volume_q.empty())
			if not self.volume_q.empty():
				self.total_volume += self.volume_q.get()
				print(self.total_volume)
			if self.total_volume_q.empty():
				self.total_volume_q.put(self.total_volume/1000)
				# print("total volume "+str(self.total_volume))
	def set_zero(self):
		self.total_volume = 0 
