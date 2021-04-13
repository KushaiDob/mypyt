# 1

def a(a_1, a_2):
    try:
        a_1, a_2 = int(a_1), int(a_2)
        a_num = a_1 / a_2
    except ValueError:
        return "Wrong Number"
    except ZeroDivisionError:
        return "Cant divide by zero"
    return round(a_num, 4)

print(a(input("Введите первое число - "), input("Введите второе число - ")))


# 2

def people_info(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city}; email - {email}; phone - {phone}"


print(people_info(name="Petr", surname="Tim", birthday="28.06.1990", city="Moscow", email="petr.tim@mail.ru", phone="332-22-32"))

# 3

def my_func(num1,num2, num3):
    return sum(sorted([num1, num2, num3])[1:])


print(my_func(1233, 444, 63))

# 4

def my_func2(x, y):
    try:
        b = x ** y
    except TypeError:
        return "Введите действительное положительное число и целое отрицательное число "
    return b

print(my_func2(66, -5))

# 5

def my_fync3():
    c = 0
    while True:
        c_list = input("Введите число, для выхода введите 'q': ").split()
        for n in c_list:
            if n == "q":
                return c
            else:
                try:
                    c += int(n)
                except ValueError:
                    print("Для выхода введите - 'q'.")
        print(f"Сумма чисел = {c}")


print(my_fync3())