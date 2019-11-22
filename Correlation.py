
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
from GOLD_2 import Gold



def AfastCorr(a):
	return np.fft.ifft(np.fft.fft(a)*np.conj(np.fft.fft(a)))




def Grafs_GOLD(nka1):  # Построение графика GOLD
	
	a = Gold(nka1)
	a = np.absolute(AfastCorr(a))

	a = np.concatenate((a[::-1], a)) # склеиваем массивы 
	tt = np.linspace((-len(a))/2, (len(a))/2, len(a))

	print(f'длина массива {len(a)}')
	print(f'maximum AKF = {max(a)}')

	dba = 20*np.log10(a)


	# Построение графиков

	fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize= (12,8), dpi = 100)
	plt.subplots_adjust(hspace =0.7 , top = 0.95)


	ax1.plot(tt, a/max(a))
	ax1.set_title('Нормированная корреляционная функция ')
	ax1.set_xlabel('Время в секундах')
	ax1.set_ylabel('Значения корреляционной функции')
	ax1.set_xticks([-1023,0, 1023])
	ax1.set_xticklabels(['-1023 дискрета','0', '1023 дискрета'])
	# ax1.axis([0, 0.000005, -1, 1])

	ax2.plot(tt, a/max(a))
	ax2.set_title('Нормированная корреляционная функция ')
	ax2.set_xlabel('Время в секундах')
	ax2.set_ylabel('Значения корреляционной функции')
	ax2.axis([-10, 10, 0.49, 1.1])
	# ax2.set_xticks([-1.48387, 0.488278])
	# ax2.set_xticklabels(['-Tд/2', 'Tд/2 '])

	# yline1 = range(-1,2)
	# xline1 = [0]*3 
	# ax2.plot(xline1, yline1)

	# yline2 = range(-1,2)
	# xline2 = [-1.48387]*3 
	# ax2.plot(xline2, yline2)

	# yline3 = [0.5]*30 
	# xline3 = range(-10,20) 
	# ax2.plot(xline3, yline3)
	# # ax2.set_yticks([0.5])
	# # ax2.set_yticklabels([0.5])



	mplcursors.cursor()

	plt.show()






if __name__ =='__main__':

	nka1 = input("Номер НКА ...")

	Grafs_GOLD(nka1)
	