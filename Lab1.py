import random

print("\nМассив со случайными числами.(Задание 1,2)")
print("-----------------------------------------------------")
n = int(input("Введите количество данных: "))
arr1 = [0]*n
miin = 9999
maax = 0

for i in range (n): #Инициализация массива
    arr1[i]=random.randint(-1000,1000)

for j in range (len(arr1)): #Цикл, вычисляющий min, max
    if miin > arr1[j]:
        miin = arr1[j]
    if maax < arr1[j]:
        maax = arr1[j]

print(list(arr1))
print("Минимальное число: ",miin," Максимальное число: ", maax," Разница(max-min): ", maax-miin)
print("-----------------------------------------------------")

print("Массив произвольного размера, вводимого с клавиатуры. (Задание 1,3)")
print("-----------------------------------------------------")
n = int(input("Введите количество данных: "))
arr = [0]*n
miin = 9999
maax = 0
for i in range (n): #Инициализация массива
    arr[i]=int(input("Введите число: ")) #Заполнение массива

for j in range (len(arr)): #Цикл, вычисляющий min, max
    if miin > arr[j]:
        miin = arr[j]
    if maax < arr[j]:
        maax = arr[j]
print(list(arr))
print("Минимальное число: ",miin," Максимальное число: ", maax," Разница(max-min): ", maax-miin)
print("-----------------------------------------------------")

print("\nСумма значений в каждой строке двумерного массива. (Задание 4)")
print("-----------------------------------------------------")

sr = int(input("Введите количество строк: "))
sl = int(input("Введите количество столбцов: "))

a = [[0]*sl]*sr
ss = []

print("\nДвумерный массив")
for i in range(len(a)): #Инициализация двумерного массива случайных чисел и суммирование данных в строках
    csum=0
    for j in range(len(a[i])):
        a[i][j] = random.randint(-1000, 1000)
        csum += a[i][j]
        print(a[i][j], end=' ')
    ss.append(csum) #Заполнение массива, в котором хранятся суммы строк
    print()
print("\nСумма элементов строк",list(ss))
print("-----------------------------------------------------")

print("\nСоздание структуры и осуществление поиска. (Задание 5)")
print("-----------------------------------------------------")

spis_sh = [["|Фамилия|","     |Имя|","   |Название факультета|","  |Номер зачетной книжки|"]] #Главный список, который потом будет заполняться + шапка

scr = True #Счетчик, как и другие scr
sch = 1 #Иммитация switch

while scr:

    spis = []

    fam = str(input("Введите Фамилию ученика: "))
    na = str(input("Введите Имя ученика: "))
    fac = str(input("Введите Название факультета ученика: "))
    zac = str(input("Введите Номер зачетной книжки ученика: "))

    fam = "|" + fam + "|"
    na = "|" + na + "|"
    fac = "|" + fac + "|"
    zac = "|" + zac + "|"

    spis.append(fam) #Добавление данных в подсписок
    spis.append(na)
    spis.append(fac)
    spis.append(zac)

    spis_sh.append(spis) #Добавление данных в список

    sch = int(input("Желаете продолжить заполнение списка? Да[1] Нет[0]: "))
    if sch == 0:
        scr = False

print('\n')

swt = True
while swt:

    for i in range(len(spis_sh)): #Цикл, выводящий данные
        for j in range(len(spis_sh[i])):
            print(spis_sh[i][j], end=' ')
        print()

    sch1 = int(input("\nЖелаете выполнить фильтрацию? Да[1] Нет[0]: "))
    if sch1 == 0:
        print("Программа выполнена успешно!")
        swt = False
    elif sch1 == 1:
        sch2 = int(input("\nЧто вы хотите найти?[0: Фамилию]; [1: Имя]; [2: Факультет]; [3: Номер зачетной книжки]: "))
        if sch2 == 0:
            fams = str(input("Введите фамилию: "))
            print(*spis_sh[0])
            for i in range(len(spis_sh)):
                for j in range(len(spis_sh[i])):
                    if fams in spis_sh[i][j]:
                        print(*spis_sh[i])
            sch3 = int(input("Желаете вернуться к списку?: Да[1] Нет[0]:"))
            if sch3 == 1:
                    print()
            else:
                print("Досвидания!")
                swt = False

        if sch2 == 1:
            nas = str(input("Введите имя: "))
            print(*spis_sh[0])
            for i in range(len(spis_sh)):
                for j in range(len(spis_sh[i])):
                    if nas in spis_sh[i][j]:
                        print(*spis_sh[i])
            sch3 = int(input("Желаете вернуться к списку?: Да[1] Нет[0]:"))
            if sch3 == 1:
                    print()
            else:
                print("Досвидания!")
                swt = False
        if sch2 == 2:
            facs = str(input("Введите Название факультета: "))
            print(*spis_sh[0])
            for i in range(len(spis_sh)):
                for j in range(len(spis_sh[i])):
                    if facs in spis_sh[i][j]:
                        print(*spis_sh[i])
            sch3 = int(input("Желаете вернуться к списку?: Да[1] Нет[0]:"))
            if sch3 == 1:
                    print()
            else:
                print("Досвидания!")
                swt = False
        if sch2 == 3:
            zacs = str(input("Введите Номер зачетной книжки: "))
            print(*spis_sh[0])
            for i in range(len(spis_sh)):
                for j in range(len(spis_sh[i])):
                    if zacs in spis_sh[i][j]:
                        print(*spis_sh[i])
            sch3 = int(input("Желаете вернуться к списку?: Да[1] Нет[0]:"))
            if sch3 == 1:
                    print()
            else:
                print("Досвидания!")
                swt = False