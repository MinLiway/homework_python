import sqlite3

menu_ = True
while menu_:
	print("""
	1. Создать БД
	2. Редактировать выбранную БД
	3. Выбрать другую БД
	4. Выход
	""")

	selection=input("Пожалуйста, выберете цифру: ") 
	
	if selection =='1': 
		path = input('Название Базы Данных: ')
		connection = sqlite3.connect(path)
		cursor = connection.cursor()
		if connection:
			connection.commit()
			
	elif selection == '2': 
		print("""
		1. SEL
		2. UP
		3. DEL
		4. Вернуться в меню
		""")
		
		sel_1 = input("Пожалуйста, выберите цифру -  ")
		if sel_1 =='1':
			select = input('SELECT: ')
			if cursor:
				com = 'SELECT %s;' %(select)
				cursor.execute(com)
				print(cursor.fetchall())
		if sel_1 == '2':
			update = input('FROM: ')
			if cursor:
				com = 'FROM %s;' %(update)
				cursor.execute(com)
				print(cursor.fetchall())
		if sel_1 == '3':
			where = input('WHERE: ')
			if cursor:
				com = 'WHERE %s;' %(where)
				cursor.execute(com)
				print(cursor.fetchall())
		elif sel_1 == '0':
			print('Возвращаю вас в меню...')
			
	elif selection == '4': 
		print("Досвидания")
		break
		
	elif selection == '3':
		path_1 = input("Пожалуйста, выберете новую Базу Данны- : ")
		connection = sqlite3.connect(path_1)
		cursor = connection.cursor()
		if connection:
			connection.commit()
	else: 
		print("Неверное значение")

cursor.close()
connection.close()
