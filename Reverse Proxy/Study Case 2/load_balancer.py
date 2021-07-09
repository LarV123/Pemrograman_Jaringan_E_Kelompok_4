import os.path
from datetime import datetime
from urllib.parse import unquote
import re

class LoadBalancer:
	def __init__(self):
		self.server_list = []
		self.server_list.append(("localhost", 8889))
		self.server_list.append(("localhost", 9000))
		self.server_list.append(("localhost", 9001))
		self.server_list.append(("localhost", 9002))
		self.server_list.append(("localhost", 9003))
		self.counter = 0
	def proses(self,data):

		forward_response = {}
		forward_response['server'] = self.server_list[self.counter]
		self.counter += 1
		if self.counter >= len(self.server_list) :
			self.counter = 0
		forward_response['request'] = data
		
		return forward_response

if __name__=="__main__": 
	load_balancer = LoadBalancer()
	for i in range(0, 100):
		d = load_balancer.proses('GET /server1/ HTTP/1.0')
		print(d)















