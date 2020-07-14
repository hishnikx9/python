# Задача №1

a = [1, "task", 1.0, {}, [], ()]
print(list(map(type, a)))

a = [1, "task", 1.0, {}, [], ()]
def my_type(el):
    for el in range(len(a)):
        print(type(a[el]))
    return
my_type(a)

# Задача №2

b = ["a", "b", "c", 123, 1.0, "task", 9, {}, 3]
j = 0
for i in range(int(len(b)/2)):
    b[j], b[j+1] = b[j+1], b[j]
    j += 2
print(b)

# Задача №3

a = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if a == 1 or a == 2 or a == 12:
    print ('Зима')
elif a == 3 or a == 4 or a == 5:
    print ('Весна')
elif a == 6 or a == 7 or a == 8:
    print ('Лето')
elif a == 9 or a == 10 or a == 11:
    print ('Осень')
else:
    print ('Ошибочка вышла')

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Я думаю ты ошибся")

# Задача №4

my_str = input("Введите строку из нескольких слов ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

# Задача №5

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (999 - выход) "))
while digit != 999:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Новый список - {my_list}")
    digit = int(input("Введите число "))

