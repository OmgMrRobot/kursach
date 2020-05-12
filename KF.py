import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from GOLD_2 import Gold



def adapter(sequence): # Меняет 0 на 1, а 1 на -1
	for i in range(len(sequence)):
		if sequence[i]== 0:
			sequence[i] = 1
		else:
			sequence[i]=-1
	return sequence

def AfastCorr(nka1):
	nka1 = adapter(nka1)
	return np.fft.ifft(np.fft.fft(nka1)*np.conj(np.fft.fft(nka1)))

def VfastCorr(nka1, nka2):
	nka1 = adapter(nka1)
	nka2 = adapter(nka2)
	return np.fft.ifft(np.fft.fft(nka1)*np.conj(np.fft.fft(nka2)))


def calc(nka1, nka2):

	nka1 = Gold(nka1)
	nka2 = Gold(nka2)

	z = np.absolute(VfastCorr(nka1.create_gold(), nka2.create_gold()))
	z = np.concatenate(( z[::-1], z))

	a = np.absolute(AfastCorr(nka1.create_gold()))
	a = np.concatenate((a[::-1], a)) # склеиваем массивы

	tt = np.linspace((-len(z))/2, (len(z))/2, len(z))

	print(f'maximum VKF = {max(z)}')
	print(f'длина массива {len(a)}')
	print(f'maximum AKF = {max(a)}')

	db = 20*np.log10(z) # по мощности
	dba = 20*np.log10(a)
	print(f'maximum VKF в db = {max(db)}')
	print(f'maximum AKF в db = {max(dba)}')

	return tt, a, z, db, dba


def Graf_VKF(nka1, nka2):

	tt, a, z, db, dba = calc(nka1, nka2)

	fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize= (16,9), dpi = 120)
	plt.subplots_adjust(hspace =0.7 , top = 0.95)

	# Чистый сигнал 

	ax1.plot(tt, a, label = f'АКФ {nka1} - {nka2}'  )
	ax1.plot(tt, z, label =  f'ВКФ {nka1} - {nka2}' )
	ax1.legend(loc = 'upper right')
	ax1.set_xlabel('Время в секундах')
	ax1.set_ylabel('Значения ВКФ')

	ax2.plot(tt, dba, label = f'АКФ {nka1} - {nka2}')
	ax2.plot(tt, db, label =  f'ВКФ {nka1} - {nka2}')
	# ax2.axis([-1040, 1040, 0, 70])
	ax2.legend(loc = 'upper right')
	ax2.set_xlabel('Время в секундах')
	ax2.set_ylabel('Значения ВКФ в db')

	mplcursors.cursor()
	plt.show()




if __name__ =='__main__':

	nka1 = input("Номер НКА ...")

	nka2 = input("Номер НКА ...")

	Graf_VKF(nka1, nka2)







