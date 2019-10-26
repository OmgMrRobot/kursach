from TML import Index , indexs
from HOW import a
import numpy as np
import itertools as it

wn = 2 # номер недели 
wn = np.binary_repr(wn, 10)

Ca_or_P_on_L2 = 0
Ca_or_P_on_L2 = np.binary_repr(Ca_or_P_on_L2, 2)

URA_index = 0 
URA_index = np.binary_repr(URA_index,4)

SVheals = 0
SVheals = np.binary_repr(SVheals,6)

IOBC = 0
IOBC = np.binary_repr(IOBC, 2)

D29 = a[-2]
D30 = a[-1]

print(D29)
print(D30)

word = wn+Ca_or_P_on_L2+URA_index+SVheals+IOBC

word = list(it.chain(word)) # разаединяю по элемента

def intager(word2 = []):
	for i in word:
		word2.append(int(i))
	return(word2)# преобразую строки в инт 

word = intager()
print(word)



lst = Index(indexs, word, D29, D30)

word3 = word+lst

print(word3)