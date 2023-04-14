# Задача №-1 к ДЗ-1


list = [0, -1, 5, 2, 3, 2, 1, 7]
count = 0
for i in range(len(list) - 1):
    if list[i] < list[i + 1]:
        count += 1

print(count)