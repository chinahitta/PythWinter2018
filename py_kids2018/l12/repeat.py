name = '' # объявили переменную, записываем в нее пустую строку
while True: # запускаем бесконечный цикл
	name = input('Здравствуйте. Как Вас зовут? ') # вводим значение переменной name с командной строки
	if name == 'Валера': # оператор условия, проверка на равенство
		print('Валера, настало твое время!') 
		break # останавливает цикл
	else:
		print('Вы нам не подходите')
