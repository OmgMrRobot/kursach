from numpy import array, arange, absolute 
from numpy.fft import rfft, rfftfreq, fft
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np
from curs2 import Gold

# s(t) = A*Gнс(t)*Gдк(t)*cos(w*t+fi)

#Fn = 1575.42  В МГц
L = 1023
T = 1 *pow(10,-3) # Длительность последовательности 
Fdk = L/T # частота последовательности = 1.023 МГц
A = 1
# Так как частота Fn очень большая, мы перенесем наш сигнал на 5 МГц - промежуточная частота 
Fn = 5 *pow(10,6) # Гц
# Частота дискретезации равна 2*Fdk  = 2.046 МГц. Чтобы влезли еще боковые липестки возьмем fs = 16Мгц
fs = 16*pow(10,6) # Гц частота дискретезация   
N = T *fs-1 # колличество элементоа в T


tt = np.arange(0, N/fs, 1/fs)

sig =  np.sin(2*pi*tt*Fn)

def CodePhaseVect(tt, Fdk):	# Ищем сколько элементов синуса умнажаются на элемент м-последовательности 
	Code =[]
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

Code = CodePhaseVect(tt, Fdk)
modulsig = ModulatedSig(sig, sequence, Code)
sig_sequence  = Sequence(sequence, Code)
# print(modulsig)
# print(len(sig))
# print(len(Code))
# print(len(modulsig))


plt.subplots(nrows = 4, ncols = 1, figsize= (12,8), dpi = 100)
plt.subplots_adjust(hspace =0.7 , top = 0.95)


# Чистый сигнал 
plt.subplot(4,1,1)
plt.plot(tt,sig)
plt.title('Чистый сигнал ')
plt.axis([0, 0.000005, -1, 1])

# последовательность
plt.subplot(4,1,2)
plt.plot(tt,sig_sequence)
plt.axis([0, 0.000005, -1.2, 1.2])

# модулированный сигнал 
plt.subplot(4,1,2)
plt.plot(tt,modulsig)
plt.title('Модулированный сигнал  ')
plt.axis([0, 0.000005, -1.2, 1.2])


# # # вычисляем преобразование Фурье. Сигнал действительный, поэтому надо использовать rfft



# # fr = (fd/2)*np.linspace(0,3,n/2)

Fourier = fft(modulsig)

fr = np.linspace(pow(10,4),fs,len(sig))

Fourier_m = absolute(Fourier)

Fourier_db = 10*np.log10(Fourier_m)

# нормированный спектр
plt.subplot(4,1,3)
plt.plot(fr, Fourier_m/max(Fourier_m))
plt.title('Нормированный спектр  ')
plt.axis([3*pow(10,6), 7*pow(10,6), 0, 1])



# нормированный спектр в dB
plt.subplot(4,1,4)
plt.plot(fr, Fourier_db/max(Fourier_db))
plt.title('Нормированный спектр в dB ')
plt.axis([3*pow(10,6), 7*pow(10,6), 0, 1])

# красная линия по уровню 13,6 дБ
plt.subplot(4,1,4)
plt.plot(range(3*pow(10,6), 7*pow(10,6)), np.ones(len(range(3*pow(10,6), 7*pow(10,6))))-0.136 , c='red')
plt.axis([3*pow(10,6), 7*pow(10,6), 0, 1])



plt.show()

# l = np.ones(30)
# g = range(30)







# plt.subplot(5,1,4)
# plt.plot(fr, X_md/max(X_md))
# plt.axis([0, 30, 0, 1])
# plt.show()