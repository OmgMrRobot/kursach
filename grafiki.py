from numpy import array, arange, absolute 
from numpy.fft import rfft, rfftfreq, fft
from math import sin, pi
import matplotlib.pyplot as plt
from numpy.random import uniform

from curs2 import Gold

n = 1023  # число элементов

fs = 1.023*pow(10,6)

fL1 = 1575.42 * pow(10,6) # Несущая частота GPS в герцах

# FD = fL1 * int(input('Введите множитель частоты дискритизации FD = fL1*...'))

FD = 4 * (fL1+fs) 

Tmax = 1023*1/FD


def adapter(sequence): # Меняет 0 на -1
	for i in range(len(sequence)):
		if sequence[i]==0:
			sequence[i]=-1
	return sequence


sequence = Gold()  # получаем нашу м-последовательность 
sequence = adapter(sequence)  # меняем 0 на -1


def sig(Tmax, FD):
#не работает 
	return [sin(2.*pi*fL1*t) for t in arange( 0,  Tmax, 1/FD)] # создаем сигнал


def modulir_sig():
	return [sig(Tmax,FD)[i]*sequence[i] for i in  range(n)] # Модулируем сигнал нашей м-последовательностью


# вычисляем преобразование Фурье. Сигнал действительный, поэтому надо использовать rfft
spectrum = rfft(modulir_sig())
smax  = absolute(max(spectrum))



def plotTime(n, FD, modulir_sig):
	# нарисуем всё это, используя matplotlib
	# Сначала сигнал зашумлённый и тон отдельно
	plt.plot(arange(n)/float(FD), modulir_sig()) # по оси времени секунды!
	plt.xlabel(u'Время, c') # это всё запускалось в Python 2.7, поэтому юникодовские строки
	plt.ylabel(u'Напряжение, мВ')
	plt.title(u'Сигнал во временной области')
	plt.grid(True)
	plt.show()
	# когда закроется этот график, откроется следующий



def plotSpectrum(n , FD, spectrum, smax):
	# Потом спектр
	plt.plot(rfftfreq(n, 1./FD), absolute(spectrum)/smax)

	plt.axis([fL1-pow(10,8) , fL1+pow(10,8), 0, 1]) # пределы по осям xmin xmax yman ymax

	# rfftfreq сделает всю работу по преобразованию номеров элементов массива в герцы
	# нас интересует только спектр амплитуд, поэтому используем abs из numpy (действует на массивы поэлементно)
	# делим на число элементов, чтобы амплитуды были в милливольтах, а не в суммах Фурье. Проверить просто — постоянные составляющие должны совпадать в сгенерированном сигнале и в спектре
	plt.xlabel(u'Частота, ГГц')
	plt.ylabel(u'Напряжение, мВ')
	plt.title(u'Спектр сигнала')
	plt.grid(True)
	plt.show()



plotTime(n,FD,modulir_sig)
plotSpectrum(n, FD,spectrum, smax)