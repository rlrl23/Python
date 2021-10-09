#Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
my_list= [number**3 for number in range(1, 1000, 2)]
print(my_list)
final_sum = 0
for number in my_list:
    sum=0
    for num in str(number):
        sum += int(num)
    if sum % 7 == 0:
        final_sum += number
print(final_sum)

#b К каждому элементу списка добавить 17
final_sum = 0
for number in my_list:
    sum=0
    number += 17
    for num in str(number):
        sum += int(num)
    if sum % 7 == 0:
        final_sum += number
print(final_sum)