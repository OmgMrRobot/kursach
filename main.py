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

sig =  A*np.sin(2*pi*tt*Fn)

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



# Построение графиков

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows = 4, ncols = 1, figsize= (12,8), dpi = 100)
plt.subplots_adjust(hspace =0.7 , top = 0.95)

# Чистый сигнал 

ax1.plot(tt, sig)
ax1.set_title('Чистый сигнал ')
ax1.set_xlabel('Время в секундах')
ax1.set_ylabel('Значения сигнала')
ax1.axis([0, 0.000005, -1, 1])


# последовательность

ax2.plot(tt,sig_sequence)
ax2.axis([0, 0.000005, -1.2, 1.2])


# модулированный сигнал 

ax2.plot(tt,modulsig)
ax2.set_title('Модулированный сигнал  ')
ax2.set_xlabel('Время в секундах')
ax2.set_ylabel('Значения сигнала')
ax2.axis([0, 0.000005, -1.2, 1.2])


# нормированный спектр

ax3.plot(fr, Fourier_m / max(Fourier_m))
ax3.set_title('Нормированный спектр  ')
ax3.set_xlabel('Частота в Гц')
ax3.set_ylabel('Амплитуда')
ax3.axis([3*pow(10,6), 7*pow(10,6), 0, 1])


# нормированный спектр в dB

spectr = ax4.plot(fr, Fourier_db - max(Fourier_db))
ax4.set_title('Нормированный спектр в dB ')
ax4.set_xlabel('Частота в Гц')
ax4.set_ylabel('Мощность в dB')
ax4.axis([3*pow(10,6), 7*pow(10,6), -50, 0])


mplcursors.cursor(spectr)

# красная линия по уровню 13,6 дБ

line = ax4.plot(range(3*pow(10,6), 7*pow(10,6)), -np.ones(len(range(3*pow(10,6), 7*pow(10,6))))-12.6 , c='red') # очень криво
ax4.axis([3*pow(10,6), 7*pow(10,6), -50, 0])

mplcursors.cursor(line)

plt.show()

