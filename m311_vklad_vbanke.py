# def bank(x,p,z):
# 	return n * factorial(n - 1)

x = int(input('Введите первоначальную сумму вклада: ' ))
p = int(input('Введите процент: ' ))
y = int(input('Введите итоговую сумму вклада: ' ))

i=0
while x < y:
	x = x*(1+p/100)//1
	i += 1

print(i)