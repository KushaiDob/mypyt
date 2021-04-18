# 1

with open('file_1.txt' , 'w', encoding='utf-8') as b:
    while True:
        line = input('Ведите данные, для окончания ввода введите пустую строку: ')
        if not line:
            break
        print(line, file=b)


# 2

with open("file_2.txt", "r", encoding='utf-8') as f_obj:
    useful = [f'{line}. {"".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк - {len(useful)}." sep="\n")

# 3

with open('file_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print (f'Средняя зп - {round(sum(employees_dict.values()) / len(employees_dict), 3)}' f'Сотрудников с средней зп менее 20000 {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

# 4

rus_write = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_44.txt", "w", encoding='utf-8') as new_file:
    with open("file_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_write.get(line.split()[0])) for line in my_file])

# 5

from random import randint

with open("file.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 500) for _ in range(500)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Сумма чисел - {sum(my_list)}")


# 6

mydict = {}
with open("file_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).strip()))
        mydict[name] = name_sum
print(f"{mydict}")