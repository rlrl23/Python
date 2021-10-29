#1 Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
import os
main_dir = 'my_project'
inside_dirs= ['settings', 'mainapp', 'adminapp', 'authapp']
for inside_dir in inside_dirs:
    dir_path = os.path.join(main_dir,inside_dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

#2 Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
import os

def create_file(file_pass):
    if not os.path.exists(file_pass):
        open(file_pass, 'w+')

def create_folders(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

with open('config.yaml', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('|--'):
            name_1 = line[3:].strip()
            if '.' in name_1:
                create_file(name_1)
            else:
                if not os.path.exists(name_1):
                    os.mkdir(name_1)

        if line.startswith('   |--'):
            name_2 = line[6:].strip()
            way = os.path.join(name_1, name_2)
            if '.' in name_2:
                create_file(way)
            else:
                create_folders(way)

        if line.startswith('   |  |--'):
            name_3 = line[9:].strip()
            way = os.path.join(name_1, name_2, name_3)
            if '.' in name_3:
                create_file(way)
            else:
                create_folders(way)

        if line.startswith('   |     |--'):
            name_4 = line[12:].strip()
            way = os.path.join(name_1, name_2, name_3, name_4)
            if '.' in name_4:
                create_file(way)
            else:
                create_folders(way)

        if line.startswith('   |        |--'):
            name_5 = line[15:].strip()
            way = os.path.join(name_1, name_2, name_3, name_4, name_5)
            if '.' in name_5:
                create_file(way)
            else:
                create_folders(way)

#3 Написать скрипт, который собирает все шаблоны в одну папку templates
import os
import shutil
root = r'my_project_2'
folder = 'templates'
dir_temp_path = os.path.join(root, folder)
if not os.path.exists(dir_temp_path):
    os.makedirs(os.path.join(root, folder))

for root, dir, files in os.walk(os.getcwd()):
    for name in dir:
        if name == 'templates':
            shutil.copytree(os.path.join(root, name), dir_temp_path, dirs_exist_ok=True)

#4 ключи — верхняя граница размера файла, а значения — общее количество файлов
import os
folder = 'some_data'
statistic = {}
key = 100000
while key > 100:
    val = len([item.stat().st_size for item in os.scandir(folder)
               if item.stat().st_size > (key//10) and item.stat().st_size < key])
    statistic[int(key)]=val
    key /=10
val = len([item.stat().st_size for item in os.scandir(folder) if item.stat().st_size < key])
statistic[int(key)] = val
print(statistic)

#5 Словарь, значения - кортежи из количества файлов опр размера и их расширения
import os
import json

folder = 'some_data'
statistic = {}
key = 100000

while key > 100:
    file_extension = [os.path.splitext(item)[1] for item in os.scandir(folder)
                          if item.stat().st_size > (key//10) and item.stat().st_size < key]
    for i, val in enumerate(file_extension, 0):
        i+=1
    statistic[int(key)] = (i, list(set(file_extension)))
    key/=10
file_extension = [os.path.splitext(item)[1] for item in os.scandir(folder)
                          if item.stat().st_size < key]

for i, val in enumerate(file_extension, 0):
    i += 1
statistic[int(key)] = (i, list(set(file_extension)))

with open('summary.json', 'w') as f:
    json.dump(statistic, f, ensure_ascii=False)