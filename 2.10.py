# '{0}, {1}, {2}'.format('a', 'b', 'c')

# '{}, {}, {}'.format('a', 'b', 'c')

# '{2}, {1}, {0}'.format('a', 'b', 'c')

# {2}, {1}, {0}'.format(*'abc')
# "Hello % s % d" % (string, num)
# s = '{0}{1}{0}'.format('abra', 'cad')

# 'Hello, {}!'.format('python')
# '{0:^100}'.format(a)

# функция принимает название и текст
#  и правильно форматирует текст
# print("{:4d}".format(88))
# print("{:2d}".format(1111))
# print("{:8.3f}".format(55.55555))
# print("{:05d}".format(44))
# print("{:08.3f}".format(33.33333))
# print("{:>10.3f}".format(22.2222))

# Function = {'Nametext': Tale, 'Text': 'how are you doing here'}


# print("{p[Text]}'s Nametext is: {p[Nametext]}".format(p=Function))


# # def format_text(title, text):
# #     print("{:^100}.format(title),"\n\t",)

# есть файл в нем имя фамилия оценка
# принимает через imput спарашивает файл и оценку
# выводит имя фамилию тех людей у кого ткая оценка и ниже

# чтение из файла tru except

# s = input("укажите файл:")
# f = open('f.txt','r')
# lines = f.readlines()
# lines = file.readlines()

# for->split()->int()
# s = input("укажите оценку")


# file = open(fname, 'r')

# lines = file.readlines()

# from os import path
 
# a = input("Введите название файла - ")
 
# if path.exists(a):
#     print('Найдено!')
#     x = int(input("введите оценку - "))
# if x < 6 and x > 4:
#     f = open('file.txt', 'r')
#     fd = f.readlines(0)
#     print(fd[0], fd[1], fd[2], fd[4], fd[5])
# else:
#     if x < 5 and x > 3:
#         f = open('file.txt', 'r')
#         fd = f.readlines(0)
#         print(fd[0], fd[2], fd[4])
#     else:
#          if x < 4 and x > 2:
#             f = open('file.txt', 'r')
#             fd = f.readlines(0)
#             print(fd[0], fd[4])


file = input('Введите файл - ')
f = open (file, 'r')
k = int(input('Введите оценку: '))
t = f.readlines()
for line in t:
    a = line.split()
    p = a[-1]
    if p == 'a':
        p = 5
    if p == 'b':
            p = 4
    if p == 'c':
            p = 3
    if p == 'd':
                    p = 2             
    b = int(p)  
    if b >= k: 
        print(a [0:2], p)

    



# file = input('Введите файл - ')

# try:
#     f = open (file, 'r')
# except:
#     print('Искал, искал не нашел')
#     exit()
# try:
#     grade = int(input('Введите оценку: '))
# except:
#     print('Это даже близко не цифра, попытайтесь еще разок')
#     exit()