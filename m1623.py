
psw = str(input('введите пароль не менее 8 символов, включая прописные и заглавные буквы: '))

while len(psw) < 8 or sum(map(str.isupper, psw)) < 1 or sum(map(str.islower, psw)) < 1:
	print('требования к паролю не выполнены: ')
	psw = input('введите пароль: ')

print('пароль принят: ')