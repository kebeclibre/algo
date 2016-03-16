#!/usr/bin/python3
# -*-coding:UTF-8 -*
import random
import time
from compteurdebug import BenchMark
from kieme import kieme
from qsMaj import quickSortCorrected, majCorrected

def main():	
	# Un tableau connu non-aléatoire
	#badExample=[1, 0, 1, 2, 0, 0] # -- FIXED !! probleme etait dans les débuts et fins des sous-tableaux
	#Custom=[5,6,7,7,8,9,9,9,9,9,9]
	#random.shuffle(Custom)
	#print(majCorrected(Custom))
	#print(majCorrected(badExample))
	# Construction du tableau aléatoire (taille,valeurMin,valeurMax)
	# Et on l'affiche
	tableToCheck=randomTABLE(11,0,10)
	print(tableToCheck)
	#print(majCorrected(tableToCheck))
	# DEBUG
	# print(Exo(Custom,Custom))
	
	#print(majCorrected(tableToCheck))
	print(kieme(tableToCheck,12))
	# On tri le tableau aléatoire
	#start=time.time()
	
	#toBench(1,0)	
	quickSortCorrected(tableToCheck)
	print(tableToCheck)
	#toBench(0,0)
	#print(majSorted(tableToCheck))
	#print(majCorrected(tableToCheck))
 	
	
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
		

def randomTABLE(size,valMin,valMax):
	result = []
	i=0
	while i < size:
		result.append(random.randrange(valMin,valMax))
		i += 1
	return result

	
main()