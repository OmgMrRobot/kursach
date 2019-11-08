import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import copy
from main import Main, sequence_main



def myCorrel(sq, kor = []): # ищет корреляцию двух сигналов
	
	sq1 = copy.deepcopy(sq)

	for _ in range(len(sq)):

		c = np.correlate(sq,sq1)[0] # перемножаем каждые элементы последовательности и складываем

		kor.append(c) # добавляем элементы в новый лист 
		sq1.insert(0,0) # двигаем вправо отностительно исходной последовательности 
		sq1.pop() # удаляем последний элемент 

	kor_left = kor[::-1] # реверсируем последовательность
	return kor_left+kor

	

def Grafs_GOLD():  # Построение графика GOLD
	sig = myCorrel(sequence_main())

	# Построение графиков

	fig, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize= (12,8), dpi = 100)
	plt.subplots_adjust(hspace =0.7 , top = 0.95)


	ax1.plot(np.arange((-len(sig)/2), len(sig)/2), sig/max(sig))
	ax1.set_title('Нормиолванная корреляционная функция ')
	ax1.set_xlabel('Время в секундах')
	ax1.set_ylabel('Значения сигнала')
	# ax1.axis([0, 0.000005, -1, 1])

	plt.show()



def Grafs_Modul_sig(): # Построение графиков
	sig = myCorrel(Main()[0]) # Берем первое значение функции Main 

	# Построение графиков

	fig, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize= (12,8), dpi = 100)
	plt.subplots_adjust(hspace =0.7 , top = 0.95)


	ax1.plot(np.arange((-len(sig)/2), len(sig)/2), sig/max(sig))
	ax1.set_title('Нормиолванная корреляционная функция модулированного сигнала ')
	ax1.set_xlabel('Время в секундах')
	ax1.set_ylabel('Значения сигнала')
	# ax1.axis([0, 0.000005, -1, 1])

	plt.show()



if __name__=='__main__':
	q = input('Gold [g] or ModulSig [m]' )
	if q == 'g':
		Grafs_GOLD()
	if q == 'm':
		print("\n Вычисляет 2 минуты!!! \n")
		Grafs_Modul_sig()
	