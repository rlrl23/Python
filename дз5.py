#генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
def odd_nums(n):
    for num in range(1, n+1, 2):
        yield num

odd_to_15 = odd_nums(15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
print(*odd_to_15)

#не используя ключевое слово yield
def odd_nums(n):
    return (num for num in range(1, n+1, 2))

odd_to_15 = odd_nums(15)
next(odd_to_15)
print(*odd_to_15)

#не используя ключевое слово yield
def odd_nums(n):
    odd_to = (num for num in range(1, n+1, 2))
    print(*odd_to)

odd_nums(20)

#генератор, возвращающий кортежи вида (<tutor>, <klass>)
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Mary', 'Kate', 'Leo']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors)>len(klasses):
    i = 0
    while i< len(tutors) - len(klasses):
        klasses.append(None)
    print(klasses)
tuple_tutors = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
next(tuple_tutors)
print(*tuple_tutors)

#вывести те элементы списка, значения которых больше предыдущего
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[i] for i in range(1, len(src)) if src[i]>src[i-1]]
print(result)

#Оптимизацию кода по памяти, по скорости, вывести уникальные числа в список
import sys
from time import perf_counter
src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = [num for num in src_2 if src_2.count(num)==1]
print(result,'\n',sys.getsizeof(result),'\n', perf_counter()-start)