
import pdb
import numpy as np
import itertools as it

Message = [] # наше сообщение

# Индексы элментов последовательности, которые нужно сложить по мод 2
indexs = {	25 : [1,2,3,5,6,10,11,12,13,14,17,18,20,23], 
			26 : [2,3,4,6,7,11,12,13,14,15,18,19,21,24], 
			27 : [1,3,4,5,7,8,12,13,14,15,16,19,20,22],  
			28 : [2,4,5,6,8,9,13,14,15,16,17,20,21,23],  
			29 : [1,3,5,6,7,9,10,14,15,16,17,18,21,22,24], 
			30 : [3,5,6,8,9,10,11,13,15,19,22,23,24]    }


def ft_Last_Bits(word, D29, D30):
	last_bits = []

	for k,v in indexs.items():
		sum_mod2 = 0
		if k == 25 or k == 27 or k == 30:
			
			for index in v: 
				sum_mod2 ^= word[index - 1]

			sum_mod2^=D29
		else:
			for index in v: 
				sum_mod2 ^= word[index - 1]
			sum_mod2^=D30
		last_bits.append(sum_mod2)
	return last_bits


def TLM_WORD():

	global Message

	preamble = [1,0,0,0,1,0,1,1] # Приамбула первые 8 бит 
	tlm_message = [0] * 16 # Заполняем сообщение 0 с 9 по 24 бит 
	D29 , D30 = [0,0]  # Значение последних двух бит предыдущего слова
	last_bits = []

	tlm_word = preamble + tlm_message # Соединяю списки
	
	last_bits = ft_Last_Bits(tlm_word, D29, D30)

	tlm_word = [i^D30 for i in tlm_word] # Перемножаем по модулю2 каждый элемент на последний бит предыдущего слова

	# print(Message + tlm_word + last_bits)
	Message = Message + tlm_word + last_bits
	# print(Message)

def HOW_WORD(sub_frame_id = 1):

	global Message

	counter = 1
	Alert_Flag = "0"
	Anti_Spoof_Flag = "0"
	last_bits = []
	D29 = Message[-2]
	D30 = Message[-1]

	sub_frame_id = np.binary_repr(sub_frame_id,3)
	counter = np.binary_repr(counter,17)
	how_word = counter + Alert_Flag +Anti_Spoof_Flag + sub_frame_id # Соединяю строки
	how_word = list(it.chain(how_word)) # разаединяю по элемента
	# D29 , D30 = Message[1,0] # Значение последних двух бит предыдущего слова
	how_word = [int(i) for i in how_word]# преобразую строки в инт 

	def D_29():
		lst = indexs[29][:-1]
		sum_mod2 = 0

		for index in lst:
			sum_mod2 ^= how_word[index - 1]
		sum_mod2 ^= D30
		if sum_mod2 == 1:
			d24 =[1]
		else:
			d24 = [0] 
		return  d24# находим значение d24

	def D_30(how_word):
		lst = indexs[30][:-1]
		sum_mod2 = 0

		for index in lst:
			sum_mod2 ^= how_word[index - 1]
		sum_mod2^=D29
		if sum_mod2 == 1:
			d23 =[1]
		else:
			d23 = [0] 

		return  d23# находим значение d23

	def Bits_23_24(word): # получаем слово с двумя упраляющими битами 
		d24 = D_29()
		d23 = D_30(word+d24)
		return word+d23+d24

	how_word = Bits_23_24(how_word)

	last_bits = ft_Last_Bits(how_word, D29, D30)

	how_word =  [j^D30 for j in how_word]
	Message = Message + how_word + last_bits
	# print(len(Message))
	# print(Message)


def Sub_frame_1():
	TLM_WORD()
	HOW_WORD(sub_frame_id = 1)

	def Word_3():
		global Message

		CA_or_P_on_L2 = 2 # используем с/a код
		ura_index = 1
		sv_health = 1
		IDOC = 1
		wn = 654
		D29 = Message[-2]
		D30 = Message[-1]
		last_bits = []

		CA_or_P_on_L2 = np.binary_repr(CA_or_P_on_L2, 2)
		ura_index = np.binary_repr(ura_index, 4)
		sv_health = np.binary_repr(sv_health, 6)
		IDOC = np.binary_repr(IDOC, 10)[:2]
		wn = np.binary_repr(wn,10)

		word = wn + CA_or_P_on_L2 + ura_index + sv_health + IDOC
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_4():
		global Message

		L2P_data_flag = [0]
		D29 = Message[-2]
		D30 = Message[-1]
		reserved = [0] * 23
		word =  L2P_data_flag + reserved
		last_bits = []

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_5():
		global Message

		reserved = [0] * 24
		D29 = Message[-2]
		D30 = Message[-1]
		word =  reserved
		last_bits = []

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_6():
		Word_5()


	def Word_7():
		global Message

		Tgd = 230
		reserved = [0] * 16
		D29 = Message[-2]
		D30 = Message[-1]
		last_bits = []

		Tgd = np.binary_repr(Tgd, 8)
		Tgd = list(it.chain(Tgd)) # разаединяю по элемента
		Tgd = [int(i) for i in Tgd]# преобразую строки в инт
		word = reserved + Tgd

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_8():
		global Message

		IDOC = 1
		Toc = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		IDOC = np.binary_repr(IDOC, 10)[2:]
		Toc = np.binary_repr(Toc, 16)
		word = IDOC + Toc

		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_9():
		global Message

		af1 = 12345
		af2 = 230
		D29 = Message[-2]
		D30 = Message[-1]

		af1 = np.binary_repr(af1, 16)
		af2 = np.binary_repr(af2, 8)
		word = af2 + af1

		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_10():
		global Message

		af0 = 1
		D29 = Message[-2]
		D30 = Message[-1]

		af0 = np.binary_repr(af0, 22)

		word = list(it.chain(af0)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в ин

		def D_29():
			lst = indexs[29][:-1]
			sum_mod2 = 0

			for index in lst:
				sum_mod2 ^= word[index - 1]
			sum_mod2 ^= D30
			if sum_mod2 == 1:
				d24 =[1]
			else:
				d24 = [0] 
			return  d24# находим значение d24

		def D_30(word):
			lst = indexs[30][:-1]
			sum_mod2 = 0

			for index in lst:
				sum_mod2 ^= word[index - 1]
			sum_mod2^=D29
			if sum_mod2 == 1:
				d23 =[1]
			else:
				d23 = [0] 

			return  d23# находим значение d23

		def Bits_23_24(word): # получаем слово с двумя упраляющими битами 
			d24 = D_29()
			d23 = D_30(word+d24)
			return word+d23+d24


		word = Bits_23_24(word)
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits
		
	Word_3()
	Word_4()
	Word_5()
	Word_6()
	Word_7()
	Word_8()
	Word_9()
	Word_10()

# def Sub_frame_2():

# 	TLM_WORD()
# 	HOW_WORD(sub_frame_id = 2)
	
Sub_frame_1()
print(Message)
print(len(Message))
