# Deprecated: j'ai découvert TABLEAU[x:y:z] après ;)
def construcTable(TABLE,a,z):
	AUX=[]
	i=0
	while a <= z:
		AUX.insert(i,TABLE[a])
		i += 1
		a += 1
	return AUX


def majoritaire(TABLE,KEEP=[]):
	debug(KEEP)
	REF=TABLE[0]
	# Nous avons besoin de la taille des sous tableaux (TABLE) pour les substitions dans leurs index
	size=len(TABLE)
	# Le tableau KEEP est l'original, sa taille (sa moitié en fait) est le repère d'arrêt des opérations
	# si KEEP est un tableau, c'est l'original, sinon, c'est la moitié de la longueur du tableau original arrondie supérieure
	
	if ( type(KEEP) == list and len(KEEP)==0 ):
		sizeToKeep=size
	elif type(KEEP) == int:
		sizeToKeep=KEEP
	else:
		return False
		
	if sizeToKeep % 2 != 0:
		halfSizeKeep=int(sizeToKeep/2 + 1)
	else:
		halfSizeKeep=int(sizeToKeep/2)

	# DEBUG	
	debug(halfSizeKeep)
	p=0
	g=size
	e=0
	i=1

	# Passage de comparaison à la REFerence
	while i < g:
		if TABLE[i] > REF:
			temp=TABLE[g-1]
			TABLE[g-1]=TABLE[i]
			TABLE[i]=temp
			g -= 1
		elif TABLE[i]==REF:
			i += 1
		else:
			temp=TABLE[e]
			TABLE[e]=TABLE[i]
			TABLE[i]=temp
			i += 1
			e += 1
			
	# Organisation du Tableau "Trié"
	# Schéma: En cours
	# ||	PETITS	|	EGAUX|	INCONNU	|	GRANDS	||
	#   0		 e            i		 g		 size
	# Schéma: Fini
	# ||	PETITS	|	EGAUX	||	GRANDS	||
	#   0		 e              i=g		 size

	# Nous pouvons commencer à regarder s'il y des morceaux plus gros que la moitié, et en déduire les opérations
	petits=TABLE[0:e]
	grands=TABLE[g:size]
	egaux=TABLE[e:g]
	volumeGrands = len(grands)
	volumeEgaux = len(egaux)
	volumePetits = len(petits)
	
	# DEBUG
	# print(TABLE)
	
	if volumeEgaux >= halfSizeKeep:
		# DEBUG
		# print "egaux"
		return (True,TABLE[e])
	elif volumePetits >= halfSizeKeep:
		# DEBUG
		# print("petits")
		# IDEE 1: On veut regarder si les petits (qui représentent plus de la moitié du tableau original) 
		# contiennent une valeur en particulier (majoritaire)
		# IDEE 2: On passe à notre fonction en récursivité le tableau original, juste pour en garder la taille. 
		# Cette taille sera le point de comparaison des sous tableaux, et donc la condition de fin des boucles
		return majoritaire(petits,sizeToKeep)
	elif volumeGrands >= halfSizeKeep:
		# Mêmes idées que pour les petits
		# DEBUG
		# print("grands")
		return majoritaire(grands,sizeToKeep)
	else:
		return (False,False)


# Deprecated
def quickSortCustom(TABLE):
	global counter
	counter += 1
	size=len(TABLE)
	if ( type(TABLE) != None and size != 0 ):
		REF=TABLE[0]
		p=0
		g=size
		e=0
		i=1

		# Passage de comparaison à la REFerence
		while i < g:
			if TABLE[i] > REF:
				temp=TABLE[g-1]
				TABLE[g-1]=TABLE[i]
				TABLE[i]=temp
				g -= 1
			elif TABLE[i]==REF:
				i += 1
			else:
				temp=TABLE[e]
				TABLE[e]=TABLE[i]
				TABLE[i]=temp
				i += 1
				e += 1
		# On récupère le tableau trié et on le divise en sous tableau pour passer chacune de ses parties non-triées au triage
		egaux=TABLE[e:g]
		petits=TABLE[0:e]
		grands=TABLE[g:size]
		
		# Le tableau Final est composé de tous les sous tableaux par récursivité
		return quickSortCustom(petits)+egaux+quickSortCustom(grands)
	else:
		# Si le sous-tableau est de type None (ou vide) on renvoi un tableau vide
		return []