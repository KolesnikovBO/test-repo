x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))

if x1 == x2 & x1 == x3:
	print(3)
elif x1 == x2 or x2 == x3 or x1 == x3:
	print(2)
else:
	print (0)
