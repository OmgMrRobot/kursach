import matplotlib.pyplot as plt
from numpy import array, arange, absolute 
from numpy.fft import rfft, rfftfreq, fft, ifft
import mplcursors
import numpy as np
from GOLD_2 import Gold



def AfastCorr(nka1):
	return np.fft.ifft(np.fft.fft(nka1)*np.conj(np.fft.fft(nka1)))

def VfastCorr(nka1, nka2):
	return np.fft.ifft(np.fft.fft(nka1)*np.conj(np.fft.fft(nka2)))


def calc(nka1, nka2): 

	a = absolute(AfastCorr(nka1))
	a = np.concatenate((a[::-1], a)) # склеиваем массивы 

	print(f'длина массива {len(a)}')
	print(f'maximum AKF = {max(a)}')



	z = absolute(VfastCorr(nka1, nka2))
	z = np.concatenate(( z[::-1], z))

	print(f'maximum AKF в db = {max(z)}')

	tt = np.linspace((-len(z))/2, (len(z))/2, len(z))

	db = 20*np.log10(z) # по мощности 
	dba = 20*np.log10(a)
	print(f'maximum AKF в db = {max(dba)}')

	return tt, a, z, db, dba


def Graf(nka1, nka2):

	tt, a, z, db, dba =  calc(nka1, nka2)

	fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize= (12,8), dpi = 100)
	plt.subplots_adjust(hspace =0.7 , top = 0.95)

	# Чистый сигнал 

	ax1.plot(tt, a, label = 'АКФ'  )
	ax1.plot(tt, z, label =  'ВКФ' )
	ax1.legend(loc = 'upper right')
	# ax1.set_title('Чистый сигнал ')
	ax1.set_xlabel('Время в секундах')
	ax1.set_ylabel('Значения ВКФ')
	# ax1.axis([-1023, 1023, min(z), max(z)+10])
	# ax1.text(2,10, 'abc', fontsize = 15)
	




	ax2.plot(tt, dba, label = 'АКФ'  )
	ax2.plot(tt, db, label =  'ВКФ')
	ax2.legend(loc = 'upper right')
	# ax2.set_title('Чистый сигнал ')
	ax2.set_xlabel('Время в секундах')
	ax2.set_ylabel('Значения ВКФ в db')
	# ax2.axis([-1023, 1023, -7, 0.1])
 


	mplcursors.cursor()
	plt.show()




if __name__ =='__main__':

	nka1 = Gold(input("Номер НКА ..."))

	nka2 = Gold(input("Номер НКА ..."))

	Graf(nka1, nka2)


# 	while True:
		
# 		nka = input('Введите номер НКА....')
# 		print("Для выхода введите q")
# 		if nka == 'q':
# 			break
		
# 		print(Gold(nka))





