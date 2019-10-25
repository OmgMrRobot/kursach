import itertools as it
import pdb

preamble = [1,0,0,0,1,0,1,1] # Приамбула первые 8 бит 

tlm_message = list(it.repeat(0,16)) # Заполняем сообщение 0 с 9 по 24 бит 

# pdb.set_trace()

word = preamble+tlm_message # Соединяю списки



D29 , D30 = [0,0]  # Значение последних двух бит предыдущего слова

indexs = {	25 : [1,2,3,5,6,10,11,12,13,14,17,18,20,23],  # Индексы элментов последовательности, которые нужно сложить по мод 2
			26 : [2,3,4,6,7,11,12,13,14,15,18,19,21,24], 
			27 : [1,3,4,5,7,8,12,13,14,15,16,19,20,22],  
			28 : [2,4,5,6,8,9,13,14,15,16,17,20,21,23],  
			29 : [1,3,5,6,7,9,10,14,15,16,17,18,21,22,24], 
			30 : [3,5,6,8,9,10,11,13,15,19,22,23,24]    }



def Index(indexs, word, lst = []): # получаем проверочные элементы последовательности. с 25 по 30
	
	
	for k,v in indexs.items():
		sum_mod2 = 0
		if k == 25 or k == 27 or k == 30: 	# мы складываем с D29 предыдущего слова
			
			for index in v: 
				sum_mod2 ^= word[index -1 ]

			sum_mod2^=D29
			
		else:								# мы складываем с D30 предыдущего слова
			for index in v: 
				sum_mod2 ^= word[index -1 ]
			sum_mod2^=D30
			

		lst.append(sum_mod2)


	return lst 

lst = Index(indexs, word)

tml_word = word+lst # соединяем 24 бита с 6 проверочными битами


print(tml_word)
print(len(tml_word))	


# pdb.set_trace()

