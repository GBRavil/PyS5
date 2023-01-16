# Напишите программу, удаляющую из текста все слова, содержащие "абв".
el = 'abc'
s = 'abcdi difg fgabc defgl'
print(s)

def write_file(name, s): # создаем отдельный файл и записываем в него строку
    with open(name, 'w') as date:
        date.writelines(s)
        date.close()
write_file('File_1.txt', s)

def read_file(): #вытаскиваем строку из файла и преобразуем с список
    with open('File_1.txt', 'r') as date:
        s = date.readlines()
        s = s[0].split()
        print(s)
        return s 
s1 = read_file()

s2 = [word for word in s1 if word.count(el)] # создаем список из слов, которые содержат 'abc' 
print(s2)
s3 = [word for word in s1 if word not in s2 ] # создаем список из слов, которые не содежат 'abc'
print(s3)



# with open('File_1.txt', 'w') as date:
#     date.writelines(s)
# with open('File_1.txt', 'r') as date:
#     s1 = date.readlines()
#     s1 = s1[0].split()
# print(s1)


