
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# import random
# n = int(input('Введите размер массива:' ))
# rand_list=[]
# for i in range(n):
#     rand_list.append(random.randint(3,9))
# print(rand_list)
# x = int(input('Введите искомое число:' ))
# count = 0
# for i in rand_list:
#     if i == x:
#         count += 1
# print(f'Число {x} встречается в массиве {count} раз')


# **Задача 18:** Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# import random
# n = int(input('Введите размер массива:' ))
# rand_list=[]
# for i in range(n):
#     rand_list.append(random.randint(3,9))
# print(rand_list)
# x = int(input('Введите искомое число:' ))
# near = rand_list[0]
# for i in rand_list:
#     if abs(i-x)< abs(near-x):
#         near = i
#     else: near = x-1
# print(near)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

rusPoint1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
rusPoint2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
rusPoint3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
rusPoint4 = ['Й', 'Ы']
rusPoint5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
rusPoint8 = ['Ш', 'Э', 'Ю']
rusPoint10 = ['Ф', 'Щ', 'Ъ']
engPoint1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
engPoint2 = ['D', 'G']
engPoint3 = ['B', 'C', 'M', 'P']
engPoint4 = ['F', 'H', 'V', 'W', 'Y']
engPoint5 = ['K']
engPoint8 = ['J', 'X']
engPoint10 = ['Q', 'Z']
N = str(input ("Введите слово: "))
N = N.upper()
res=0
for i in N:
    if (i in rusPoint1):
        res=res+1
    if (i in rusPoint2):
        res=res+2
    if (i in rusPoint3):
        res=res+3
    if (i in rusPoint4):
        res=res+4
    if (i in rusPoint5):
        res=res+5
    if (i in rusPoint8):
        res=res+8
    if (i in rusPoint10):
        res=res+10
    if (i in engPoint1):
        res=res+1
    if (i in engPoint2):
        res=res+2
    if (i in engPoint3):
        res=res+3
    if (i in engPoint4):
        res=res+4
    if (i in engPoint5):
        res=res+5
    if (i in engPoint8):
        res=res+8
    if (i in engPoint10):
        res=res+10
print (res)