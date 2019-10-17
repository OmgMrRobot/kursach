from numpy import array, arange, absolute 
from numpy.fft import rfft, rfftfreq, fft
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np
from curs2 import Gold


def adapter(sequence): # Меняет 0 на -1
	for i in range(len(sequence)):
		if sequence[i]==0:
			sequence[i]=-1
		# else:
		# 	sequence[i]=0
	return sequence

n = 1023
f = 15.7542 
fd = 1023
t = np.arange(0, 99, 1/fd)
j = pow(-1, 0.5)
T = 0.001 # длительнось последовательности 1мс


N = round((T/n)*2*f)



x = np.sin(2*pi*t*f)


plt.subplot(5,1,1)
plt.plot(t,x)
plt.axis([0,0.4, -1,1])



sequence = Gold()  # получаем нашу м-последовательность 
sequence = adapter(sequence)  # меняем 0 на -1
sequence2 = []

sequence3 =[]






for i in sequence:
	for j in range(99):
		sequence2.append(i)


plt.subplot(5,1,2)
plt.plot(t,sequence2)



y = [sequence2[i]*x[i] for i in range(len(sequence2)) ]




plt.subplot(5,1,2)
plt.plot(t,y)
plt.axis([0, 0.4, -1.5, 1.5 ])



# # вычисляем преобразование Фурье. Сигнал действительный, поэтому надо использовать rfft



# fr = (fd/2)*np.linspace(0,3,n/2)

X = fft(y)

fr = np.linspace(0,512,len(x)/2)

X_m = absolute(X[0:np.size(fr/2)])


plt.subplot(5,1,3)
plt.plot(fr, X_m/max(X_m))
plt.axis([0, 30, 0, 1])



X_md = 10*np.log10(X_m)

l = np.ones(30)
g = range(30)



plt.subplot(5,1,4)
plt.plot(g, l-0.13 , c = 'red')
plt.ylabel('0.87')
plt.axis([0, 30, 0, 1])




plt.subplot(5,1,4)
plt.plot(fr, X_md/max(X_md))
plt.axis([0, 30, 0, 1])
plt.show()