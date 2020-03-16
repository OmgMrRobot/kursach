import pdb
import numpy as np
import itertools as it
from math import pi as PI


class Class_Data():
	"""docstring for ClassName"""
	def __init__(self, Id, health, eccentricity, corr_to_inclination, 
		rate_of_right_ascention, square_root_of_semi_major_axis, right_ascention_parameter,
		argument_of_perigee, mean_anomaly, Af0m,  Af1, Af0l, week_almanac,
		time_of_week_almanac ):

		self.Id = Id
		self.health = health
		self.eccentricity = eccentricity
		self.corr_to_inclination = corr_to_inclination
		self.rate_of_right_ascention = rate_of_right_ascention
		self.square_root_of_semi_major_axis = square_root_of_semi_major_axis
		self.right_ascention_parameter = right_ascention_parameter
		self.argument_of_perigee = argument_of_perigee
		self.mean_anomaly = mean_anomaly
		self.Af0m = Af0m
		self.Af1 = Af1
		self.Af0l = Af0l
		self.week_almanac = week_almanac
		self.time_of_week_almanac = time_of_week_almanac






		

# Data = []
# lst = [x for x in range(1500)]

# g = 0
# for i in range(32):
# 	Data.append(type('New_Class_Data%d' % i, (), 
# 	{'Id': lst[g],
# 	 'health' : lst[g + 1],
# 	 'eccentricity' : lst[g + 2],
# 	 'time_of_week_almanac' : lst[g + 13] } ))
# 	g += 13






def ft_parser():
	my_file = open("001.txt", "r") 
	string = my_file.read()
	my_file.close()

	string2 = []
	lst = [] # лист для значений
	Data = [] # лист для экземпляров класса
	index = 0

	string = string.split("GPS: ")  # разделяем по GPS:

	# print(string)

	for i in string: # разделяем по \n
		string2 = string2 + i.split('\n')

	string = [] # очистили лист

	for j in range(1, len(string2)):  # разделяем по =
		if (len(string2[j])):
			string = string + string2[j].lstrip().split('=')	

	for r in range(1, len(string), 2): # оставляем только значение
		lst.append(string[r]) 

	for i in range(round(len(lst)/14)): # создаем экземпляры класса и запаминаем
		data = Class_Data(lst[index], lst[index + 1], lst[index + 2],
		 lst[index + 3], lst[index + 4], lst[index+ 5], lst[index + 6],
		 lst[index +7], lst[index + 8], lst[index + 9], lst[index + 10],
		 lst[index + 11], lst[index + 12], lst[index + 13])

		Data.append(data)
		index += 14

	# for i in Data:
	# 	print(i.Id)

	return (Data)


def separate_bits(word):

	word = list(it.chain(word))
	word = [int(i) for i in word]
	return word


def swich_to_bits():

	Data = ft_parser()

	for i  in Data:
		i.eccentricity = int( (float(i.eccentricity) / PI) / (2**(-21)))
		i.corr_to_inclination =  int ((float(i.corr_to_inclination) / (2*PI)) / (2**(-19)))
		i.rate_of_right_ascention = int ((float(i.rate_of_right_ascention) / PI) / (2**(-38)) * 1000) #???
		i.square_root_of_semi_major_axis = int (float(i.square_root_of_semi_major_axis) / (2**(-11)))
		i.right_ascention_parameter = int((float(i.right_ascention_parameter) / PI) / (2**(-23)))
		i.argument_of_perigee = int((float(i.argument_of_perigee) / PI) / (2**(-23)))
		i.mean_anomaly = int((float(i.mean_anomaly) / PI) / (2**(-23)))
		i.Af0m = int(float(i.Af0m) / (2**(-20)) / 1000) # в секундах
		i.Af1 = int(float(i.Af1) / (2**(-38))) # в секундах
		# i.time_of_week_almanac = separate_bits(np.binary_repr(float(time_of_week_almanac), ))

	for i in Data:
		i.Id = separate_bits(np.binary_repr(int(i.Id), 6))
		i.health = separate_bits(np.binary_repr(int(i.health), 8))
		i.eccentricity = separate_bits(np.binary_repr(i.eccentricity, 16))
		i.corr_to_inclination = separate_bits(np.binary_repr(i.corr_to_inclination, 16))
		i.rate_of_right_ascention = separate_bits(np.binary_repr(i.rate_of_right_ascention, 16))
		i.square_root_of_semi_major_axis = separate_bits(np.binary_repr(i.square_root_of_semi_major_axis, 24))
		i.right_ascention_parameter = separate_bits(np.binary_repr(i.right_ascention_parameter, 24))
		i.argument_of_perigee = separate_bits(np.binary_repr(i.argument_of_perigee, 24))
		i.mean_anomaly = separate_bits(np.binary_repr(i.mean_anomaly, 24))
		i.Af0m = separate_bits(np.binary_repr(i.Af0m, 11))
		i.Af1 = separate_bits(np.binary_repr(i.Af1, 11))
	# 	# i.week_almanac = separate_bits(np.binary_repr(float(week_almanac), ))
	# 	# i.time_of_week_almanac = separate_bits(np.binary_repr(float(time_of_week_almanac), ))


	# a = 0
	# for i in Data:
	# 	print(i.rate_of_right_ascention)
	# 	a+=1
	# print(a)
	return (Data)


if __name__ == "__main__":
	swich_to_bits()

