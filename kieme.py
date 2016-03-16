from qsMaj import partition
from implBench import debug

def kiemeAux(table,debut,fin,k):
	(e,g) = partition(table,debut,fin)
		
	if e == k:
		debug("eq")
		return table[e]
	elif e > k:
		debug("sup")
		return kiemeAux(table,debut,e,k)
	elif e < k:
		debug("inf")
		return kiemeAux(table,e+1,len(table),k)
			
def kieme(table,k):
	k -= 1
	if k < len(table):
		""" 
		idee 1 placer le k cherché en kieme position et vérifier en fin de parcours si il est legitime à sa place
		ca va prendre du temps si on trouve pas du premier coup.
		idee 2: faire comme majoritaire MAIS apres partition checker si le volume des petits est sup ou egal à k
		si oui le kieme est dans petits, sinon si e est egal à k, le pivot etait le kieme
		sinon il est dans les grands
		dans le cas petit et grand on recommence 
		"""
		return kiemeAux(table,0,len(table),k)
		
	else:
		return False
