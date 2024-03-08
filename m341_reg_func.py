import json

def add_user (log_pas):
	with open('reg_file.json', 'r') as reg_file:
		log_pas = json.load(reg_file)
	log = str(input('Введите логин: '))
	pas = str(input('Введите пароль: '))
	if log not in log_pas:
		log_pas[log] = pas
	else:
		print('login already exist')
		return 1 #отдаем 1 при продолжении функции
	with open('reg_file.json', 'w') as reg_file:
		json.dump(log_pas, reg_file)
	return 0 #отдаем 0 при завершении функции

log_pas = {}
while True:
	result = add_user (log_pas)
	if result == 0:
		break

# 	return shopping_list
# 	with open('reg_file.json', 'a') as reg_file:
# 		json.dump(login + ':')
# 		reg_file.write(passw + ',')



# def register(log_pas):
# log = str(input('Введите логин: '))
# pas = str(input('Введите пароль: '))

# reg = register(log, pas)

