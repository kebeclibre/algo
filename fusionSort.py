from qsMaj import swap
from implBench import debug



def fusionSort(table):
	return fuFinal(table)
	#return fusionAux(table,0,len(table))
	#fusionSortAux(table,0,len(table))

	
def fuFinal(table):
	if len(table) > 1:
		left=fuFinal(table[:len(table)//2])
		right=fuFinal(table[len(table)//2:])
		return merge(left,right)
	elif len(table) ==1:
		return table
	else:
		return []
		

def fusionAux(table,debut,fin): # DEPRECATED
	if fin-debut > 1:
		debug(debut)
		debug(fin)
		debug(fin//2)
		left=table[0:len(table)//2]
		right=table[len(table)//2:len(table)]
		leftAux=fusionAux(left,0,len(left))
		rightAux=fusionAux(right,0,len(right))
		debug(left)
		debug(right)
		return merge(left,right)

		#return merge(fusionAux(table,debut,fin // 2),fusionAux(table,fin // 2,fin))
	elif fin-debut ==1:
		return merge(table,[])
	else:
		return []
		
	
def merge(table1,table2):
	if ( len(table1) == 0 and len(table2) == 0 ):
		return []
	elif len(table1) == 0:
		return table2
	elif len(table2) == 0:
		return table1
	else:
		i=0
		j=0
		tableMerged=[]
		while i < len(table1) and j < len(table2):
			if table1[i] <= table2[j]:
				tableMerged.append(table1[i])
				i += 1
			else:
				tableMerged.append(table2[j])
				j += 1
				
		tableMerged.extend(table1[i:])
		tableMerged.extend(table2[j:])
		return tableMerged