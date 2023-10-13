import os.path
import time


def lensort():
    strlist = input("Введите строки через пробел: ").split()
    sorted_strlist = sorted(strlist, key=lambda length: len(length))
    print(strlist, sorted_strlist)
    return


def unique():
    strlist = input("Введите строки через пробел: ").split()
    s = set(strlist)
    print(s)
    return


def my_enumerate():
    strlist = input("Введите строки через пробел: ").split()
    numlist = list(i for i in range(len(strlist)))
    z = zip(numlist, strlist)
    print(*z)
    return


def func_4():
    strlist = input("Введите имя файла с расширением .txt: ").split()
    if len(strlist) != 1:
        print("Неверный формат ввода")
        return
    file_name = strlist[0]
    file_spl = file_name.split('.')
    if len(file_spl) != 2 or file_spl[1] != "txt":
        print("Неверный формат имени файла")
        return
    current_dir = os.getcwd()
    if not os.path.isfile(os.path.join(current_dir, file_name)):
        print("Файл не существует", os.path.join(current_dir, file_name))
        return
    with open(os.path.join(current_dir, file_name), 'r') as f:
        data = f.readlines()
    f_dict = {}
    for d in data:
        for word in d.split():
            if word not in f_dict:
                f_dict[word] = 1
            else:
                f_dict[word] = f_dict[word] + 1
    print(f_dict)
    return


def decorator():
    # num_list = [i + i % 3 for i in range(10000000)]
    strlist = input("Введите числа через пробел: ").split()
    num_list = [int(i) for i in strlist]
    first_func_res = list()
    f_start = time.time()
    for i in num_list:
        first_func_res.append(i*i)
    f_end = time.time()
    print(f_end - f_start)
    f_start = time.time()
    second_func_res = list(i*i for i in num_list)
    f_end = time.time()
    print(f_end - f_start)
    f_start = time.time()
    third_func_res = list(map(lambda i: i*i, num_list))
    f_end = time.time()
    print(f_end - f_start)


# lensort()
# unique()
# my_enumerate()
# func_4()
decorator()
