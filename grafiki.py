from numpy import array, arange, absolute 
from numpy.fft import rfft, rfftfreq, fft
from math import pi
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from GOLD_2 import Gold

# s(t) = A*Gнс(t)*Gдк(t)*cos(w*t+fi)

#Fn = 1575.42  В МГц частота сигнала GPS
L = 1023
T = 1 *pow(10,-3) # Длительность последовательности 
Fdk = L/T # частота последовательности = 1.023 МГц
A = 1
# Так как частота Fn очень большая, мы перенесем наш сигнал на 5 МГц - промежуточная частота 
Fn = 5 *pow(10,6) # Гц
# Частота дискретезации равна 2*Fdk  = 2.046 МГц. Чтобы влезли еще боковые липестки возьмем fs = 16Мгц
fs = 16*pow(10,6) # Гц частота дискретезация   
N = T *fs-1 # колличество элементоа в T


tt = np.arange(0, N/fs, 1/fs)  # Время для сигнала

sig =  np.sin(2*pi*tt*Fn)

def CodePhaseVect(tt, Fdk, Code = []):	# Ищем сколько элементов синуса умнажаются на элемент м-последовательности 

	for i in tt:
		c = int(i*Fdk) # Округление в меньшую сторону для получения индекса м-последовательности
		#  Возможно надо умножить Fdk на 2
		Code.append(c)
	return Code


def adapter(sequence): # Меняет 0 на 1, а 1 на -1
	for i in range(len(sequence)):
		if sequence[i]==0:
			sequence[i]=1
		else:
			sequence[i]=-1
	return sequence


def ModulatedSig(sig, sequence, Code, modulsig = []):# Модулирует сигнал м-последовательностью
	for i in range(len(sequence)):
		for j in range(len(Code)):
			if i == Code[j]:
				modulsig.append(sig[j]*sequence[i])
	return modulsig

def Sequence(sequence, Code, sequence2 = []): # дублирует значения м-последовательности 
	for i in range(len(sequence)):
		for j in range(len(Code)):
			if i == Code[j]:
				sequence2.append(sequence[i])
	return sequence2



sequence = Gold()  # получаем нашу м-последовательность 
sequence = adapter(sequence)  # меняем 0 на -1

Code = CodePhaseVect(tt, Fdk) # Ищем сколько элементов синуса умнажаются на элемент м-последовательности
modulsig = ModulatedSig(sig, sequence, Code) # Модулирует сигнал м-последовательностью
sig_sequence  = Sequence(sequence, Code)  # дублирует значения м-последовательности


Fourier = fft(modulsig) #вычисляем преобразование Фурье.

fr = np.linspace(pow(10,4),fs,len(sig)) # создаем массив частот 

Fourier_m = absolute(Fourier) #вычисляем действительный значения /  sqrt((a)^2+(ib)^2)  

Fourier_db = 20*np.log10(Fourier_m) # по мощности 



plt.subplots(nrows = 4, ncols = 1, figsize= (12,8), dpi = 100)
plt.subplots_adjust(hspace =0.7 , top = 0.95)

# Чистый сигнал 
plt.subplot(4,1,1)
plt.plot(tt,sig)
plt.title('Чистый сигнал ')
plt.xlabel('Время в секундах')
plt.ylabel('Значения сигнала')
plt.axis([0, 0.000005, -1, 1])

# последовательность
plt.subplot(4,1,2)
plt.plot(tt,sig_sequence)
plt.axis([0, 0.000005, -1.2, 1.2])

# модулированный сигнал 
plt.subplot(4,1,2)
plt.plot(tt,modulsig)
plt.title('Модулированный сигнал  ')
plt.xlabel('Время в секундах')
plt.ylabel('Значения сигнала')
plt.axis([0, 0.000005, -1.2, 1.2])


# нормированный спектр
plt.subplot(4,1,3)
plt.plot(fr, Fourier_m / max(Fourier_m))
plt.title('Нормированный спектр  ')
plt.xlabel('Частота в Гц')
plt.ylabel('')
plt.axis([3*pow(10,6), 7*pow(10,6), 0, 1])

# fig, ax =  plt.subplots(4,1,4)

# нормированный спектр в dB
plt.subplot(4,1,4)
plt.plot(fr, Fourier_db - max(Fourier_db))
plt.title('Нормированный спектр в dB ')
plt.xlabel('Частота в Гц')
plt.ylabel('')
plt.axis([3*pow(10,6), 7*pow(10,6), -50, 0])

# красная линия по уровню 13,6 дБ
plt.subplot(4,1,4)
plt.plot(range(3*pow(10,6), 7*pow(10,6)), -np.ones(len(range(3*pow(10,6), 7*pow(10,6))))-12.6 , c='red') # очень криво
plt.axis([3*pow(10,6), 7*pow(10,6), -50, 0])

# mplcursors.cursor(spectr)

plt.show()

