# Напишите программу, удаляющую из текста все слова, содержащие "абв".
el = 'abc'
s1 = 'abcdi difg fgabc defgl'
print(s1)

s1 = s1.split()
print(s1)

s2 = [word for word in s1 if word.count(el)] # создаем список из слов, которые содержат 'abc' 
print(s2)

s3 = [word for word in s1 if word not in s2 ] # создаем список из слов, которые не содежат 'abc' варинат 1
# s3 = list(set(s1).difference(s2)) # создаем список из слов, которые не содежат 'abc' варинат 2
# s3 = list(filter(lambda x: x not in s2, s1)) # создаем список из слов, которые не содежат 'abc' варинат 3
print(s3)
