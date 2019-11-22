

def G1(): #х-базовое состояние

	lst = []
	x = [1,1,1,1,1,1,1,1,1,1]  #х-базовое состояние

	for _ in range(1023):
	#  на следующей итерации х и lst  поменяются 
		r3 = x[2] 			# берем значение 3ого регистора
		r10 = x[9]			# берем значение 10 ого регистора 
		x.insert(0, r3^r10)	# перемножаем 3 регистор и 10 регистор и ставим на первое место в массив
		r = x.pop()			# удаляем постледний элемент из листа регистров и возвращяем его
		lst.append(r) 		# добавляем его в лист М-последовательност

	return lst

# print(OneItaration())




def G2i(nka): # х-базовое состояние

	
	x = [1,1,1,1,1,1,1,1,1,1] # х-базовое состояние
	lst = []

	num = { '1':[2,6],'2':[3,7],'3':[4,8],'4':[5,9],'5':[1,9],'6':[2,10],'7':[1,8],'8':[2,9],'9':[3,10],
		'10':[2,3],'11':[3,4],'12':[5,6],'13':[6,7],'14':[7,8],'15':[8,9],'16':[9,10],'17':[1,4],'18':[2,5],
		'19':[3,6],'20':[4,7],'21':[5,8],'22':[6,9],'23':[1,3],'24':[4,6],'25':[5,7],'26':[6,8],'27':[7,9],'28':[8,10],
		'29':[1,6],'30':[2,7],'31':[3,8],'32':[4,9],
		} # значения нка

	n = num.get(nka) # присваиввет n лист из двух чисел(номеров регистров)

	for _ in range(1023):
		r2 = x[1]			# берем значение 2ого регистора
		r3 = x[2] 			# берем значение 3ого регистора
		r6 = x[5]			# берем значение 6ого регистора
		r8 = x[7]			# берем значение 8ого регистора
		r9 = x[8]			# берем значение 9ого регистора
		r10 = x[9]        	# берем значение 10ого регистора 

		#Создаем последовательность G2i
		first = x[n[0]-1] # чило в первом регисторе
		second = x[n[1]-1] # чило во втором региторе
		lst.append(first^second)


		x.insert(0, r2^r3^r6^r8^r9^r10)	# перемножаем 2,3,6,8,9,10 регистор по модулю и ставим на первое место в массив
		r = x.pop()			# удаляем постледний элемент из листа регистров и возвращяем его

	return lst  		# возвращаем значения регистров и М - последовательности



def Gold(nka): # Выводит код голда
	lst = []
	g1 = G1() 		#  G1 м-последовательность

	g2i = G2i(nka)			#  G2i м-последовательность


	for i in range(len(g1)): # перемножаем по элементно две последовательности 
		n1 = g1[i]
		n2 = g2i[i]
		mod =  n1^n2
		lst.append(mod)

	return lst



if __name__ =='__main__':

	while True:
		
		nka = input('Введите номер НКА....')
		print("Для выхода введите q")
		if nka == 'q':
			break
		
		print(Gold(nka))


