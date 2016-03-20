from qsMaj import swap
from implBench import debug


def fusionSort(table):
	fusionAux(table,0,len(table))
	#fusionSortAux(table,0,len(table))
	
def fusionAux(table,debut,fin):
	if fin-debut >= 2:
		left=fusionAux(table,debut,fin // 2)
		right=fusionAux(table,fin // 2+1,fin)
		return merge(left,right)
	else:
		return []
		
		
	
def fusionSortStableAttempt(table,debut,fin):
	if (debut < fin):
		if fin-debut > 2:
			fusionSortStableAttempt(table,debut,fin // 2)
			fusionSortStableAttempt(table,fin // 2,fin)
			mergeOnPlace(table,debut,fin)
		elif fin-debut == 2:
			if table[debut] > table[fin-1]:
				swap(table,debut,fin-1)
	#elif len(table) == 
		
		
	
def merge(table1,table2):
	if len(table1) == 0:
		return table2
	elif len(table2) == 0:
		return table1
	elif ( len(table1) == 0 and len(table2) == 0 ):
		return []
	else:
		i=0
		j=len(table1)
		lenTable2=len(table2)
		table1.append(table2)
		while i < len(table1) and j < lenTable2:
			if table1[i] <= table1[j]:
				swap(table1,i+1,j)
				j += 1
			elif table1[i] > table1[j]:
				swap(table1,i,j)
				i += 1
		return table1
		
def mergeOnPlace(table,debut,fin):
	lenPortion=fin-debut
	i=debut
	halfPortion=lenPortion // 2
	j=halfPortion
	if lenPortion > 1:
		while i < halfPortion and j < lenPortion:
			debug(i)
			debug(table[i])
			debug(j)
		
			debug(table[j])
		
			if table[i] <= table[j]:
				swap(table,i+1,j)
				j += 1
			elif table[i] > table[j]:
				swap(table,i,j)
				i += 1