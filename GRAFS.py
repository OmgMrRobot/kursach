from numpy import array, arange, absolute
from numpy.fft import rfft, rfftfreq, fft
from math import pi
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from GOLD_2 import Gold



# s(t) = A*Gнс(t)*Gдк(t)*cos(w*t+fi)

# Fn = 1575.42  В МГц частота сигнала GPS

class CreateSpectrum(Gold):

    def __init__(self, NKA):

        super().__init__(NKA)
        self.L = 1023
        self.T = 1 * pow(10, -3)  # Длительность последовательности
        self.Fdk = self.L / self.T  # частота последовательности = 1.023 МГц
        self.A = 1
        # Так как частота Fn очень большая, мы перенесем наш сигнал на 5 МГц - промежуточная частота
        self.Fn = 5 * pow(10, 6)  # Гц
        # Частота дискретезации равна 2*Fdk  = 2.046 МГц. Чтобы влезли еще боковые липестки возьмем fs = 16Мгц
        self.fs = 16 * pow(10, 6)  # Гц частота дискретезация
        self.N = self.T * self.fs - 1  # колличество элементоа в T
        self.tt = np.arange(0, self.N / self.fs, 1 / self.fs)  # Время для сигнала
        self.sig = self.A * np.sin(2 * pi * self.tt * self.Fn)


    def adapter(self, sequence):  # Меняет 0 на 1, а 1 на -1
        for i in range(len(sequence)):
            if sequence[i] == 0:
                sequence[i] = 1
            else:
                sequence[i] = -1
        return sequence

    def CodePhaseVect(self):  # Ищем сколько элементов синуса умнажаются на элемент м-последовательности
        # Округление в меньшую сторону для получения индекса м-последовательности
        #  Возможно надо умножить Fdk на 2
        return [int(i * self.Fdk) for i in self.tt]

    def ModulatedSig(self,  sequence, Code):  # Модулирует сигнал м-последовательностью
        modulsig = []
        for i in range(len(sequence)):
            for j in range(len(Code)):
                if i == Code[j]:
                    modulsig.append(self.sig[j] * sequence[i])
        return modulsig

    def Sequence(self, sequence, Code):  # дублирует значения м-последовательности
        sequence2 = []
        for i in range(len(sequence)):
            for j in range(len(Code)):
                if i == Code[j]:
                    sequence2.append(sequence[i])
        return sequence2

    def caller(self):

        sequence = self.adapter(self.create_gold())  # меняем 0 на -1  получаем нашу м-последовательность

        Code = self.CodePhaseVect()  # Ищем сколько элементов синуса умнажаются на элемент м-последовательности
        modulsig = self.ModulatedSig( sequence, Code)  # Модулирует сигнал м-последовательностью
        sig_sequence = self.Sequence(sequence, Code)  # дублирует значения м-последовательности

        Fourier = fft(modulsig)  # вычисляем преобразование Фурье.

        fr = np.linspace(pow(10, 4), self.fs, len(self.sig))  # создаем массив частот

        Fourier_m = absolute(Fourier)  # вычисляем действительный значения /  sqrt((a)^2+(ib)^2)

        Fourier_db = 20 * np.log10(Fourier_m)  # по мощности

        return sig_sequence, modulsig, Fourier_m, Fourier_db , fr


    def grafs(self):

        sig_sequence, modulsig, Fourier_m, Fourier_db, fr = self.caller()

        # Построение графиков

        fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(12, 8), dpi=100)
        plt.subplots_adjust(hspace=0.7, top=0.95)

        # Чистый сигнал

        ax1.plot(self.tt, self.sig)
        ax1.set_title('Чистый сигнал ')
        ax1.set_xlabel('Время в секундах')
        ax1.set_ylabel('Значения сигнала')
        ax1.axis([0, 0.000005, -1, 1])

        # последовательность

        ax2.plot(self.tt, sig_sequence)
        ax2.axis([0, 0.000005, -1.2, 1.2])

        # модулированный сигнал

        ax2.plot(self.tt, modulsig)
        ax2.set_title('Модулированный сигнал  ')
        ax2.set_xlabel('Время в секундах')
        ax2.set_ylabel('Значения сигнала')
        ax2.axis([0, 0.000005, -1.2, 1.2])

        # нормированный спектр

        ax3.plot(fr, Fourier_m / max(Fourier_m))
        ax3.set_title('Нормированный спектр  ')
        ax3.set_xlabel('Частота в Гц')
        ax3.set_ylabel('Амплитуда')
        ax3.axis([3 * pow(10, 6), 7 * pow(10, 6), 0, 1])

        # нормированный спектр в dB

        spectr = ax4.plot(fr, Fourier_db - max(Fourier_db))
        ax4.set_title('Нормированный спектр в dB ')
        ax4.set_xlabel('Частота в Гц')
        ax4.set_ylabel('Мощность в dB')
        ax4.axis([3 * pow(10, 6), 7 * pow(10, 6), -50, 0])

        mplcursors.cursor(spectr)

        # красная линия по уровню 13,6 дБ

        line = ax4.plot(range(3 * pow(10, 6), 7 * pow(10, 6)), -np.ones(len(range(3 * pow(10, 6), \
                                                                                  7 * pow(10, 6)))) - 12.6,
                        c='red')  # очень криво
        ax4.axis([3 * pow(10, 6), 7 * pow(10, 6), -50, 0])

        mplcursors.cursor(line)

        plt.show()




if __name__ == "__main__":

    create = CreateSpectrum(input('Введите номер НКА....'))
    create.grafs()
