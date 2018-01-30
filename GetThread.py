import threading
import time
import datetime
import urllib
import json

class GetThread(threading.Thread):
	def __init__(self):
		super(GetThread, self).__init__()
		self.hz = 0
		self.num_client = 0
		self.power = 0
		self.stop_ = 0

	def stop(self):
		self.stop_ = 1

	def run(self):
		while self.stop_ == 0:
			(self.hz, self.num_client, self.power) = self.get()

	def get(self):
		url = "http://acchub.net:8080/"
		result = None
		try :
			result = urllib.urlopen( url ).read()
			j = json.loads(result)
			return ((float)(j["hz"]), (int)(j["num_client"]), (float)(j["power"]))
		except ValueError :
			print("error connect")
