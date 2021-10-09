#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
duration = int(input("Введите продолжительность в секундах") )
if duration < 60:
    print (duration, "сек")
elif duration == 60:
    print("1 мин")
elif duration < 360:
    min = duration // 60
    sec = duration % 60
    print(min,"мин", sec, "сек")
elif duration == 360:
    print("1 час")
elif duration < 86400:
    hour = duration//3600
    min = (duration % 3600)//60
    sec = (duration % 3600) % 60
    print(hour, "час", min, "мин", sec, "сек")
elif duration == 86400:
    print("1 день")
else:
    day = duration//86400
    hour = (duration % 86400)//3600
    min = ((duration % 86400)% 3600)//60
    sec = ((duration % 86400) % 3600) % 60
    print(day, "дн", hour, "час", min, "мин", sec, "сек")

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

#Реализовать склонение слова «процент» во фразе «N процентов»
for percent in range(1, 101):
    if percent == 11 or percent == 12 or percent == 13 or percent == 14:
        print(percent, 'процентов')
    elif percent ==1 or percent %10 ==1:
        print (percent, 'процент')
    elif percent % 10 >1 and percent % 10 <5:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')