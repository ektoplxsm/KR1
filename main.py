from random import random


neg = zero = pos = 0
negative = null = positive = 0
M = []

for i in range(1, 10):
    m = int(random() * 10) - 1
    M.append(m)
    print(m, end=' ')
    if m > 0:
        pos += 1
    elif m < 0:
        neg += 1
    else:
        zero += 1

s = sum([m for m in M if m < 0])

print("\nОтрицательных: ", neg)
print("Равных нулю: ", zero)
print("Положительных: ", pos)
print("Минимальное :", min(M))
print("Сумма отрицательных элементов :", s)
print("...")


for j in range(1, 10):
    m = int(random() * 10) - 1
    M.append(m)
    print(m, end=' ')
    if m > 0:
        positive += 1
    elif m < 0:
        negative += 1
    else:
        null += 1

s = sum([m for m in M if m < 0])

print("\nОтрицательных: ", negative)
print("Равных нулю: ", null)
print("Положительных: ", positive)
print("Минимальное :", min(M))
print("Сумма отрицательных элементов :", s)
print("...")

line = input("Введите числа:\n").split()
cnt = 0
for i, s in enumerate(line):
    if s.isdigit():
        x = i
        cnt += len(s)
        del line[x]
print("Количество цифр:", cnt)

# result = 0

# while True:
#     try:
#         value = (input('Введите числа,как надоест - нажмите точку:'))
#         result += len(value)
#     except ValueError:
#         print(f'Была обнаружена точка. Количество: {result}')
#         break
#     except KeyboardInterrupt:
#         print(f'\nКоличество: {result}')
# break
