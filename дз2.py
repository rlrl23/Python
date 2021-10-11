#Выяснить тип результата выражений:
print(type(15*3))
print(type(15/3))
print(type(15//2))
print(type(15**2))

#Обособить каждое целое число кавычками и дополнить нулём
my_list= ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list =[]
for element in my_list:
    if element[0] in '1234567890':
        element = f'{int(element):02d}'
        new_list.extend(['"', element, '"'])
    elif element[0] in '+-' and element[1] in '1234567890':
        sign = element[0]
        number = element[1:]
        new_list.extend(['"',sign+ f'{int(number):02d}', '"'])
    else:
        new_list.append(element)
print(new_list)
#Сформировать из обработанного списка строку
print(' '.join(new_list))

#Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
workers= ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in workers:
    name = worker.split(' ')[-1].title()
    print("Привет, ", name,'!')

# Цены и сортировка
prices = [57.8, 46.51, 97, 23.4, 56, 79.99, 100, 5.3, 31.5, 32.1, 99.99]
result = ""
for price in prices:
    if isinstance(price, int) == True:
        coins = 0
    else:
        parts_price = str(price).split('.')
        coins = int(parts_price.pop())
    result += f'{int(price)} руб {coins:02d} коп, '
print(result)
# цены, отсортированные по возрастанию
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
# цены, отсортированные по убыванию
new_prices = sorted(prices, reverse = True)
print(new_prices)
#цены пяти самых дорогих товаров по возрастанию
print(prices[5:-1])