
import pdb
import numpy as np
import itertools as it
from Parser import swich_to_bits

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

def free_word(): # Пустое слово
	global Message

	reserved = [0] * 24
	D29 = Message[-2]
	D30 = Message[-1]
	word =  reserved
	last_bits = []

	last_bits = ft_Last_Bits(word, D29, D30)
	word =  [j^D30 for j in word]
	Message = Message + word + last_bits



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

def Sub_frame_2():

	TLM_WORD()
	HOW_WORD(sub_frame_id = 2)

	def Word_3():
		global Message

		IODE = 230
		Crc = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		IODE = np.binary_repr(IODE, 8)
		Crc = np.binary_repr(Crc, 16)


		word = IODE + Crc
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_4():
		global Message

		delta_n = 12345
		M0 = 1
		D29 = Message[-2]
		D30 = Message[-1]

		delta_n = np.binary_repr(delta_n, 16)
		M0 = np.binary_repr(M0, 32)[:8]

		word = delta_n + M0
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_5():
		global Message

		M0 = 1

		M0 = np.binary_repr(M0, 32)[8:]
		D29 = Message[-2]
		D30 = Message[-1]

		word = M0
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_6():
		global Message
		
		D29 = Message[-2]
		D30 = Message[-1]
		Cuc = 12345
		e = 12345

		Cuc = np.binary_repr(Cuc, 16)
		e = np.binary_repr(e, 32)[:8]

		word = Cuc + e
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_7():
		global Message
		
		D29 = Message[-2]
		D30 = Message[-1]
		e = 12345

		e = np.binary_repr(e, 32)[8:]

		word = e
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_8():
		global Message
		
		D29 = Message[-2]
		D30 = Message[-1]
		Cus = 12345
		A = 12345

		Cus = np.binary_repr(Cus, 16)
		A = np.binary_repr(A, 32)[:8]

		word = Cus + A
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_9():
		global Message
		
		D29 = Message[-2]
		D30 = Message[-1]
		A = 12345

		A = np.binary_repr(A, 32)[8:]

		word = A
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_10():
		global Message
		
		D29 = Message[-2]
		D30 = Message[-1]
		Toe = 1245
		Fit_Interval_Flag = 0
		AODO = 0

		Toe = np.binary_repr(Toe, 16)
		AODO = np.binary_repr(AODO, 5)
		Fit_Interval_Flag = np.binary_repr(Fit_Interval_Flag, 1)

		word = Toe + Fit_Interval_Flag + AODO 
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт

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

def Sub_frame_3():

	TLM_WORD()
	HOW_WORD(sub_frame_id = 3)

	def Word_3():
		global Message

		Cic = 230
		right_ascen_at_week  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		right_ascen_at_week  = np.binary_repr(right_ascen_at_week, 32)[:8]
		Cic = np.binary_repr(Cic, 16)


		word = Cic + right_ascen_at_week
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_4():
		global Message

		right_ascen_at_week  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		right_ascen_at_week  = np.binary_repr(right_ascen_at_week, 32)[8:]

		word = right_ascen_at_week
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_5():
		global Message

		Cis = 230
		i  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		i  = np.binary_repr(i, 32)[:8]
		Cis = np.binary_repr(Cis, 16)


		word = Cis + i
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_6():
		global Message

		I  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		I  = np.binary_repr(I, 32)[8:]

		word = I
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_7():
		global Message

		Crc = 230
		w  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		w  = np.binary_repr(w, 32)[:8]
		Crc = np.binary_repr(Crc, 16)


		word = Crc + w
		word = list(it.chain(word)) 
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_8():
		global Message

		w  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		w  = np.binary_repr(w, 32)[8:]

		word = w
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_9():
		global Message

		dqdt  = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		dqdt  = np.binary_repr(dqdt, 24)

		word = dqdt
		word = list(it.chain(word))
		word = [int(i) for i in word]
		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits


	def Word_10():
		global Message

		IODE  = 123
		IDOT = 12345
		D29 = Message[-2]
		D30 = Message[-1]

		IODE  = np.binary_repr(IODE, 8)
		IDOT  = np.binary_repr(IDOT, 14)

		word = IODE + IDOT
		word = list(it.chain(word)) # разаединяю по элемента
		word = [int(i) for i in word]# преобразую строки в инт

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

def Sub_frame_4():

	TLM_WORD()
	HOW_WORD(sub_frame_id = 4)

	def Word_3_9():
		for i in range(7):
			free_word()

	def Word_10():
		global Message

		D29 = Message[-2]
		D30 = Message[-1]

		word = [0] * 22


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

	Word_3_9()
	Word_10()


def Sub_frame_5(Data):
	TLM_WORD()
	HOW_WORD()


	def Word_3(): #alarm
		global Message
		data_id = [0] * 2
		sv_id = [0] * 6

		word = data_id + sv_id + Data.eccentricity
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits
		

	def Word_4():  #alarm
		global Message
		Toa = [0] * 8

		word = Toa + Data.corr_to_inclination[:16] #!!!!!!
		# print(Data.corr_to_inclination)
		# print(len(Data.corr_to_inclination))
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_5():
		global Message

		word = Data.rate_of_right_ascention + Data.health
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_6():
		global Message

		word = Data.square_root_of_semi_major_axis
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_7():
		global Message

		word = Data.right_ascention_parameter
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_8():
		global Message

		word = Data.argument_of_perigee
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_9():
		global Message

		word = Data.mean_anomaly
		D29 = Message[-2]
		D30 = Message[-1]

		last_bits = ft_Last_Bits(word, D29, D30)
		word =  [j^D30 for j in word]
		Message = Message + word + last_bits

	def Word_10():
		global Message

		word = Data.Af0m[:8] + Data.Af1 + Data.Af0m[8:]
		D29 = Message[-2]
		D30 = Message[-1]

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
	Word_4() # kos
	Word_5()
	Word_6()
	Word_7()
	Word_8()
	Word_9()
	Word_10()





	


def Main_Message():

	Data = swich_to_bits()
	Sub_frame_1()
	Sub_frame_2()
	Sub_frame_3()

	for i in range(24):
		Sub_frame_4()
		Sub_frame_5(Data[i])
	# страница 25 с состоянием спутников
	Sub_frame_4()
	Sub_frame_4()



Main_Message()
print(Message)
print(len(Message))