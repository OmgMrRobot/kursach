import pdb
import numpy as np
import itertools as it
from math import pi, sqrt 


def separate_bits(word):

	word = list(it.chain(word))
	word = [int(i) for i in word]
	return word

def Move_to_Bits_Ephemeris(almanah):
	almanah["Toe"] = "error"
	almanah["Diff"] = "error"


	almanah["e"] = int((almanah["e"] / pi) / (2**(-33)))
	almanah["i"] =  int((almanah["i"] / pi) / (2**(-31)))
	almanah["dqdt"] = int((almanah["dqdt"] / pi) / (2**(-43)) * 1000) #???
	almanah["A"] = int(sqrt(almanah["A"]) / (2**(-19)))
	almanah["right_ascen_at_week"] = int((almanah["right_ascen_at_week"] / pi) / (2**(-31)))
	almanah["w"] = int((almanah["w"] / pi) / (2**(-31)))
	almanah["m"] = int((almanah["m"] / pi) / (2**(-31)))

	almanah["Cic"] = int((almanah["Cic"]) / (2**(-29)))
	almanah["Cis"] = int((almanah["Cis"]) / (2**(-29)))

	almanah["Crc"] = int((almanah["Crc"]) / (2**(-5)))
	almanah["Crs"] = int((almanah["Crs"]) / (2**(-5)))

	almanah["Cuc"] = int((almanah["Cuc"]) / (2**(-29)))
	almanah["Cus"] = int((almanah["Cus"]) / (2**(-29)))

	almanah["af0"] = int(almanah["af0"] / (2**(-31)) / 1000) # в секундах
	almanah["af1"] = int(almanah["af1"] / (2**(-43))) 

	almanah["Tgd"] = int(almanah["Tgd"] / (2**(-31)) / 1000)



	almanah["e"] = separate_bits(np.binary_repr(almanah["e"], 32))
	almanah["i"] = separate_bits(np.binary_repr(almanah["i"], 32))
	almanah["dqdt"] = separate_bits(np.binary_repr(almanah["dqdt"], 24))
	almanah["A"] = separate_bits(np.binary_repr(almanah["A"], 32))
	almanah["right_ascen_at_week"] = separate_bits(np.binary_repr(almanah["right_ascen_at_week"], 32))
	almanah["w"] = separate_bits(np.binary_repr(almanah["w"], 32))
	almanah["m"] = separate_bits(np.binary_repr(almanah["m"], 32))

	almanah["Cic"] = separate_bits(np.binary_repr(almanah["Cic"], 16))
	almanah["Cis"] = separate_bits(np.binary_repr(almanah["Cis"], 16))

	almanah["Crc"] = separate_bits(np.binary_repr(almanah["Crc"], 16))
	almanah["Crs"] = separate_bits(np.binary_repr(almanah["Crs"], 16))

	almanah["Cuc"] = separate_bits(np.binary_repr(almanah["Cuc"], 16))
	almanah["Cus"] = separate_bits(np.binary_repr(almanah["Cus"], 16))

	almanah["af0"] = separate_bits(np.binary_repr(almanah["af0"], 22))
	almanah["af1"] = separate_bits(np.binary_repr(almanah["af1"], 16))

	almanah["Tgd"] = separate_bits(np.binary_repr(almanah["Tgd"], 8))



