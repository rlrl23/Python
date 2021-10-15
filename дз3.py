# перевод чисел с заглавной буквы и без
def num_translate_adv(num):
    translation = {'zero':'ноль','one' : 'один', 'two': 'два', 'three' : 'три', 'four' : 'четыре','five': 'пять',
 'six':'шесть', 'seven':'семь', 'eight': 'восемь', 'nine':'девять', 'ten':'десять'}
    if num.istitle():
       print(translation.get(num.lower()).title())
    else:
        print(translation.get(num))

num_translate_adv("one")

#"И": ["Иван", "Илья"], "М": ["Мария"], "П": ["Петр"]
def thesaurus(*names):
    # Сортируя имена - получаем сортировку по ключу:
    names = list(names)
    names.sort()
    saurus = {}
    key =[]
    for name in names:
        val = [name]
        if name[0] in key:
            val.append(names[key.index(name[0])])
        key.append(name[0])
        saurus[name[0]] = val
    print(saurus)

thesaurus("Марфа", "Павел", "Иван", "Мария", "Петр", "Илья")

from random import choice
"""Функция возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков
  Аргумент repeat_w - разрешает или запрещает повторы слов в шутках
  Своеобразно обработано исключение"""
def get_jokes(num, repeat_w='no'):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke=[]
    while num>0:
        noun = choice(nouns)
        adverb = choice(adverbs)
        abjective = choice(adjectives)
        joke.append(f'{noun} {adverb} {abjective}')
        num -=1
        if repeat_w == 'no' and num<=4:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(abjective)
        else:
            print('Максимальное количество уникальных шуток - 5!')
            break
    print(joke)
get_jokes(num=6, repeat_w='no')
