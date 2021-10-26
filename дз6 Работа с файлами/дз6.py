#1 распарсить файл логов web-сервера, получить список кортежей
import requests

response = (requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')).text

with open('response.txt', 'w+', encoding='utf-8') as f:
    f.write(response)
    lines = response.split(')"')
    for line in lines:
        ind_addr = line.find('- -')
        remote_addr = line[: ind_addr]
        ind_start = line.find('"')
        ind_end = line.find('HTTP')
        request_type_resource = line[ind_start:ind_end].replace('"','')
        result = (remote_addr, request_type_resource)
        with open('result.txt', 'a+', encoding='utf-8') as r:
            r.writelines(tuple(result))

#2 Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
addr_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ind_addr = line.find(' - -')
        remote_addr = line[: ind_addr]
        addr_list.append(remote_addr)
with open('ip.txt', 'w+', encoding='utf-8') as f:
    f.writelines(addr_list)
    dict_addr = {}
    for addr in addr_list:
        if addr not in dict_addr:
            count = addr_list.count(addr)
            dict_addr[addr] = count
    print(dict_addr)
    max_val = 1
    for key, val in dict_addr.items():
        if val > max_val:
            max_val = val
            spammer = key
print(spammer)

#3 Новый документ содержащий словарь: ключи — ФИО, значения — данные о хобби из др файлов
from itertools import zip_longest

with open ('users.csv', 'r', encoding='utf-8') as n, open ('hobby.csv', 'r', encoding='utf-8') as h:
    name_hobby = {}
    for names, hobbys in zip_longest(n, h):
        if isinstance(names, str):
            name = names.replace(',',' ').strip()
        else:
            exit(code=1)
        if isinstance(hobbys, str):
            hobby = hobbys.strip()
        else: hobby = None
        name_hobby[name] = hobby

print(name_hobby)

#4 Новый документ содержащий словари на каждого юзера
from itertools import zip_longest
import json
name_hobby_all =[]
with open ('users.csv', 'r', encoding='utf-8') as n, open ('hobby.csv', 'r', encoding='utf-8') as h:
    for names, hobbys in zip_longest(n, h):
        name_hobby = {}
        if isinstance(names, str):
            name = names.strip()
            surname, name, father_name = name.split(',')
        else:
            exit(code=1)
        if isinstance(hobbys, str):
            hobby = hobbys.strip()
            if ',' in hobby:
                hobby= hobby.split(',')
        else: hobby = None
        name_hobby['Фамилия'] = surname
        name_hobby['Имя'] = name
        name_hobby['Отчество'] = father_name
        name_hobby['Хобби'] = hobby
        name_hobby_all.append(name_hobby)
with open('name_hobby_all.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(name_hobby_all, ensure_ascii=False))