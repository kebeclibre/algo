import time

class BenchMark:
	
	def __init__(self):
		self.compteur = 0
		self.startTime = time.time()
		self.stopTime = 0
		self.duration = 0
# 		self.nomFBenchmark = ""
		
	def increment(self):
		#if type(self) != None:
		self.compteur += 1
		
	def stop(self):
		print("Nombre d'appels: {}".format(self.compteur))
		self.stopTime= time.time()
		self.duration = self.stopTime - self.startTime
		print("Temps écoulé: {}".format(self.duration))
		
# 	def setFunBench(self, nom):
# 		self.nomFBenchmark = nom