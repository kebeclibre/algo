#!/usr/bin/python3
# -*-coding:UTF-8 -*
import random
import time
from compteurdebug import BenchMark

bench=1
DEBUG=0
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
	
		
def main():	
	# Un tableau connu non-aléatoire
	#badExample=[1, 0, 1, 2, 0, 0] # -- FIXED !! probleme etait dans les débuts et fins des sous-tableaux
	#Custom=[5,6,7,7,8,9,9,9,9,9,9]
	#random.shuffle(Custom)
	#print(majCorrected(Custom))
	#print(majCorrected(badExample))
	# Construction du tableau aléatoire (taille,valeurMin,valeurMax)
	# Et on l'affiche
	tableToCheck=randomTABLE(5,0,10)
	print(tableToCheck)
	#print(majCorrected(tableToCheck))
	# DEBUG
	# print(Exo(Custom,Custom))
	
	#print(majCorrected(tableToCheck))
	
	# On tri le tableau aléatoire
	#start=time.time()
	
	toBench(1,0)	
	quickSortCorrected(tableToCheck)
	print(tableToCheck)
	toBench(0,0)
	
	print(majCorrected(tableToCheck))
 	
	
	# BENCHMARK : FONCTIONS NON CORRIGEES QS
	# T(1000000)=34s
	# Avec 1263777 appels à la fonction en récursion
	# n*ln (n) = 14*10^6
	# occupe 30Mo
	# T(100000)=3s
	# Avec 190451 appels à la fonction
	# n*ln (n) = 1,1*10^6
	# occupe 6Mo
	
	# BENCHMARK: FONCTIONS CORRIGEES QS
	# T(100000) = 3,2 s
	# 190000 appels recursifs
	# Occupe 5Mo
	# T(1000000)=34s
	# 1264177 appels
	# Occupe 19Mo
		
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
	toBench(2,0)
	if (debut < fin):
		(e,g) = partition(table,debut,fin)
		qsAux(table,debut,e)
		qsAux(table,g,fin)
		
def quickSortCorrected(table):
	qsAux(table,0,len(table))
		
	
def randomTABLE(size,valMin,valMax):
	result = []
	i=0
	while i < size:
		result.append(random.randrange(valMin,valMax))
		i += 1
	return result


# Deprecated: j'ai découvert TABLEAU[x:y:z] après ;)
def construcTable(TABLE,a,z):
	AUX=[]
	i=0
	while a <= z:
		AUX.insert(i,TABLE[a])
		i += 1
		a += 1
	return AUX

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
		
main()