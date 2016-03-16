bench=1
DEBUG=1
benches=[]

def debug(message):
	global DEBUG
	if DEBUG == 1:
		print(message)

def toBench(status,index):
	#if name == "qs":
	toBenchAuxQs(status,index)
	#elif name == "maj":
	#	toBenchAuxMaj(status,index)

def toBenchAuxQs(status,index):
	global bench
	global benches
	if bench == 1: 
		if status == 1:
			benches[index] = BenchMark()
		elif status == 0 :
			benches[index].stop()
		elif status == 2:
			benchQs[index].increment()	
			
def toBenchAuxMaj(status):
	global bench
	global benchMaj
	if bench == 1: 
		if status == 1:
			benchMaj = BenchMark()
		elif status == 0 :
			benchMaj.stop()
		elif status == 2:
			benchMaj.increment()			
	
		