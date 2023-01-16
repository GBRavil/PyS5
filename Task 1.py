# Напишите программу, удаляющую из текста все слова, содержащие "абв".
el = 'абв'
s1 = 'абвгд гдеё абвуг ждуп'.split()
print(s1)
s2 = [word for word in s1 if word.count(el)]
print(s2)
s3 = [word for word in s1 if word not in s2 ]
print(s3)