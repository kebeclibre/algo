def swap(table,i,j):
	temp=table[j]
	table[j]=table[i]
	table[i]=temp


def partition(table,debut,fin):
	pivot=table[debut]
	p=debut
	g=fin
	e=debut
	i=debut + 1

	# Passage de comparaison à la REFerence
	while i < g:
		if table[i] > pivot:
			g -= 1
			swap(table,i,g)
		elif table[i]==pivot:
			i += 1
		else:
			swap(table,i,e)
			i += 1
			e += 1
	return (e, g)
	
	
def qsAux(table,debut,fin):
	#toBench(2,0)
	if (debut < fin):
		(e,g) = partition(table,debut,fin)
		qsAux(table,debut,e)
		qsAux(table,g,fin)
	
		
def quickSortCorrected(table):
	qsAux(table,0,len(table))
	
		
def majCorrected(table):
	return majAux(table,0,len(table),len(table) // 2 +1)
	
	
def majAux(table,debut,fin,tailleRef):
		debug(tailleRef)
		(e,g)=partition(table,debut,fin)

		if g-e >= tailleRef:
			debug("egaux")
			return (True,table[e])
		elif e >= tailleRef:
			debug("petits")
			return majAux(table,debut,e,tailleRef)
		elif fin-g >= tailleRef:
			debug("grands")
			return majAux(table,g,fin,tailleRef)
		else:
			return (False,False)
			
def majSorted(table):
	marching=True
	sizeCumul=1
	sizeCurrent=1
	compare=table[0]
	i=0
	halfSize=len(table) // 2 +1
	
	while marching or sizeCumul <= halfSize:
		if table[sizeCumul] == compare:
			debug("equal")
			debug(table[sizeCumul])
			marching=True
			sizeCurrent += 1
			if sizeCurrent >= halfSize:
				return (True, table[sizeCumul])
				break
			sizeCumul += 1
		elif table[sizeCumul] != compare:
			compare = table[sizeCumul]
			marching=False
			sizeCumul += 1
			sizeCurrent = 1
	
	return (False,False)