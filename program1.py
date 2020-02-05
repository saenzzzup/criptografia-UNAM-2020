import fileinput

suma = sum(float(num) for num in fileinput.input())

if (suma).is_integer():
	print(int(suma))
else:
	print(suma)