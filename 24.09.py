# f=open('C://Users//min//my_project//text.txt', 'w')
# print(f.write('GGGGGGGGGGGGGG'))
# f.close()

# f=open('C://Users//min//my_project//text.txt', 'a')
# print(f.write("DDDDDDDDDDD"))
# f.close()

# f=open('C://Users//min//my_project//text.txt', 'r')
# str_list = f.readlines()
# print(str_list)
# f.close()

# f=open('C://Users//min//my_project//text.txt', 'w')
# f.writelines(['BBBBBBBBBBBBB', 'AAAAAAAAAAAA'])
# f.close()

# f=open('C://Users//min//my_project//text.txt', 'r')

# f = open('C://Users//min//my_project//text.txt', 'r')
# lines = f.readlines()
# lines = [line[:-1] for line in lines]
# d = {lines[1]:lines[2], lines[3]: int(lines[4])}
# print(d)
# f.close()

ip = { }
f = open('C://Users//min//my_project//text.txt', 'r')
p = f.readlines()
l = 0
for i in range(len(p)):
    if i % 2 == 0:
        v = p[i][:-1]
    else:
        if i !=len(p):
            l=p[i]
        else:
            l=p[i][:-1]
        ip[v]=l
print(ip)
f.close()

