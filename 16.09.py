d = {}
p = '+7-777-777-77-77'

def validate_number(p):  
    # функция проверки валидатности номеров
         if len(p) !=16:
            #  если длина номера не 16 выводится ложь
                  return False
         if p[0:3] !='+7-':
            #  если первые три цифры не +7- выводится ложь
                  return False
         if p[6] !='-' or p[10] !='-' or p[13] !='-':
            #  если 6, 10, 13 знаки номера не - выводится ложь
                  return False
         ba = p[3:6] + p[7:10] + p[11:13] + p[14:]
         digits = '0123456789'
        #  цифры в промежутках должны равнятся 123456789
         for sym in ba:
                  if not sym in digits:
                           return False
                  return True
                #   если равняется выводится правда, если нет ложь
print(validate_number(p))
# вывести валидатный номер
def add_to_book(name, phone):
    # функция добавить в книгу
         d[name] = phone
         return d
while True:
         name = (input(' имя: ')) 
        #  с клавиатуры имя
         if name == 'q' :
                  print(d)
                  break
         phone = (input(' введите номер:'))
        #  с клавиатуры номер
         if phone == 'q' :
                  print(d)
                  break
         if validate_number(phone):
                  print ('number is okay, additing to book')
                  add_to_book(name, phone)
                  print('new phone added')
                #   проверка номера 
         else:
                  print('namber is incorrect, please give another')
                  
       
       