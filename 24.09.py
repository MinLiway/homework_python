# f=open('text.txt', 'r')
# print(f.read())
# f.close()

# f=open('text.txt', 'w')
# f.write('poka')
# f.close()

# f=open('text.txt', 'a')
# f.write('privet')
# f.close()

# f=open('text.txt', 'w')
# f.writelines(['BBBBBBBBBBBBB', 'AAAAAAAAAAAA'])
# f.close()

# f = open('text.txt')
# print(f.readlines())
# f.close()

f = open('file.txt', 'r')
lines = f.readlines()
lines = [line[:-1] for line in lines]
dict_ = {'ip': lines[2][:-1], 'port': int(lines[4][:-1])}
d = {lines[1]:lines[2], lines[3]: int(lines[4])}
print(d)
f.close()