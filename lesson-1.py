# 1

a = "Hi"
b = "friend!"
print(f"{a}, {b}")
name = input("Your name:")
surname = input("Your surname")
print(f"Good to see you, {name} {surname}!")

# 2

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# 3

n = input("Введите число: ")
print(f"{n} + {n + n} + {n + n +n} = {int(n) + int(n + n) + int(n + n + n)}")

# 4

num_init = int(input("Введите число: "))
greatest_dig = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10

print(f"Самая большая цифра в числе {num_init} равна {greatest_dig}")

# 5

q = float(input("Введите сумму выручки:"))
e = float(input("Введите сумму издержек:"))
r = q - e
if r > 0:
    print(f"Отлично вы в плюсе на {- r}")
    print(f"Рентабильность выручки составила {100 * r / q:.1f}%")
    p = int(input("Сколько человек в вашей компании?"))
    print(f"Если вы раздадите прибль, то каждый получит {r / p:.3f}")
elif r < 0:
    print(f"Вы работаете с убытком в {- r}")
else:
    print("Вы хотя бы не в минусе!")

# 6

while True:
    days = 1
    start_km = float(input("Результат в начале:"))
    last_km = float(input("Результат в конце:"))
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьется результата за {days} дней")
        break
