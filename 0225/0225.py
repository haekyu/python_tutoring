# Enumerate

lst = [2, 3, 1, 2, 5]

for th, e in enumerate(lst):
	print('%d-th element=%d' % (th, e))


# Zip
name_lst = ["berry", "HK", "MK", "JH"]
age_lst = [0.5, 27, 27, 27]
addr_lst = ["a", "a", "a", "a"]

for n, ag, ad in zip(name_lst, age_lst, addr_lst):
	print(n, ag, ad)


import pandas

df = pandas.read_csv('data.csv', sep=',')
info_dict = {}

# for th in range(0, 5, 1):
# 	name = df['이름'][th]
# 	age = df['나이'][th]
# 	addr = df['주소'][th]

# 	info_dict[name] = [age, addr]

# print(info_dict)

for name, age, addr in zip(df['이름'], df['나이'], df['주소']):
	info_dict[name] = [age, addr]

print(info_dict)



# f = open('data.csv', 'r', encoding='utf8')
# lines = f.readlines()
# f.close()

# name_age_dict = {}

# th = 0
# for line in lines:
# 	if th == 0:
# 		th = th + 1
# 		continue

# 	lst = line.split(',')
# 	print('%d-th line:' % th, lst)
# 	name = lst[0]
# 	age = float(lst[1][:-1])

# 	print('name = %s, age = %.2lf' % (name, age))

# 	name_age_dict[name] = age

# 	th = th + 1
# print(name_age_dict)


# f = open('newfile.txt', 'a')
# f.write('Hi Hello\n')
# f.write('I am fine thank you!')
# f.write('....?????')
# f.close()


# f = open('data.csv', 'r', encoding='utf8')
# while True:
# 	line = f.readline()
# 	print(line)
# 	if line == "":
# 		break



# print(lines)


# lines = f.readlines()
# f.close()

# print(lines)

'''
name_age_dict = {}

name_age_dict['Berry'] = 0.5
name_age_dict['EDIYA'] = 3

print(name_age_dict)

berry_age = name_age_dict['Berry']

print('Berry' in name_age_dict)

print('해규' in name_age_dict)
print(name_age_dict.values())
print(name_age_dict.keys())

'''
'''
sss = "Berry Berry! Berry."

num = 0

# lst = sss.split()
lst = ["Hi", "Berry", "Berry!!!", "Berry."]

for word in lst:
	if word[0:5] == "Berry":
		num = num + 1
	
lst = []

for i in range(1, 21, 1):
	if 20 % i == 0:
		lst.append(i)

for i in range(1, 21, 1):
	if 20 % i != 0:
		continue
	lst.append(i)

'''
