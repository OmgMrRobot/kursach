

with open("Message12.txt", mode = "r") as file:
	lst = file.read()

with open("Message.txt", mode = "r") as file:
	lst2 = file.read()

if lst == lst2:
	print("Равны")
else:
	print("Не равны")