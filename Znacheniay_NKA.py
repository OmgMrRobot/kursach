


num = { '1':[2,6],
		'2':[3,7],
		'3':[4,8],
		'4':[5,9],
		'5':[1,9],
		'6':[2,10],
		'7':[1,8],
		'8':[2,9],
		'9':[3,10],
		'10':[2,3],
		'11':[3,4],
		'12':[5,6],
		'13':[6,7],
		'14':[7,8],
		'15':[8,9],
		'16':[9,10],
		'17':[1,4],
		'18':[2,5],
		'19':[3,6],
		'20':[4,7],
		'21':[5,8],
		'22':[6,9],
		'23':[1,3],
		'24':[4,6],
		'25':[5,7],
		'26':[6,8],
		'27':[7,9],
		'28':[8,10],
		'29':[1,6],
		'30':[2,7],
		'31':[3,8],
		'32':[4,9],
		}

for k,v in num.items():
	v[0] = 10 - v[0]
	v[1] = 10 - v[1]

