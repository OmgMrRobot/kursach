import itertools as it
import pdb
import numpy as np

counter = 1

Alert_Flag = '0'
Anti_Spoof_Flag ='0'
sub_frame_id = 1
sub_frame_id = np.binary_repr(1,3)

counter = np.binary_repr(counter,17)

word = counter + Alert_Flag +Anti_Spoof_Flag + sub_frame_id # Соединяю строки

word = list(it.chain(word)) # разаединяю по элемента


def intager(word2 = []):
	for i in word:
		word2.append(int(i))
	return(word2)# преобразую строки в инт 


word = intager()

D29 , D30 = [1,0] # Значение последних двух бит предыдущего слова



indexs = {	25 : [1,2,3,5,6,10,11,12,13,14,17,18,20,23], # Индексы элментов последовательности, которые нужно сложить по мод 2
			26 : [2,3,4,6,7,11,12,13,14,15,18,19,21,24], 
			27 : [1,3,4,5,7,8,12,13,14,15,16,19,20,22],  
			28 : [2,4,5,6,8,9,13,14,15,16,17,20,21,23],  
			29 : [1,3,5,6,7,9,10,14,15,16,17,18,21,22,24], 
			30 : [3,5,6,8,9,10,11,13,15,19,22,23,24]    }



# print(word)
# print(len(word))

def D_29(sum_mod2 = 0):
	lst = indexs[29][:-1]
	# print(lst)

	for index in lst:
		sum_mod2 ^= word[index -1 ]
	sum_mod2 ^= D30
	if sum_mod2 == 1:
		d24 =[1]
	else:
		d24 = [0] 

	return  d24# находим значение d24



def D_30(word, sum_mod2 = 0):
	lst = indexs[30][:-1]
	# print(lst)

	# print(word)
	# print(len(word))
	for index in lst:
		sum_mod2 ^= word[index -1 ]
	sum_mod2^=D29

	# print(sum_mod2)
	if sum_mod2 == 1:
		d23 =[1]
	else:
		d23 = [0] 

	return  d23# находим значение d23



def Word24(word): # получаем слово с двумя упраляющими битами 
	d24 = D_29()
	d23 = D_30(word+d24)
	return word+d23+d24


# print(Word24(word))
# print(len(Word24(word)))



def Index(indexs, lst = []): # получаем проверочные элементы последовательности. с 25 по 30
	
	word2 = Word24(word)  # получаем слово с двумя упраляющими битами 
	for k,v in indexs.items():
		sum_mod2 = 0
		if k == 25 or k == 27 or k == 30:
			
			for index in v: 
				sum_mod2 ^= word2[index -1 ]

			sum_mod2^=D29
			
		else:
			for index in v: 
				sum_mod2 ^= word2[index -1 ]
			sum_mod2^=D30
			

		lst.append(sum_mod2)


	return word2 + lst # соединяем 24 бита с 6 проверочными битами

a = Index(indexs)
print(a)
print(len(a))