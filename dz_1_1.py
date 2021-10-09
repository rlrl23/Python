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