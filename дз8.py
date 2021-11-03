#1
import re

url = 'someone@geekbrains.ru'
try:
    name_domain = re.search(r"(?P<username>[a-z0-9]+)@(?P<domain>[a-z0-9]+\.[a-z]+)", url)
    print(name_domain.groupdict())
except AttributeError:
    print('wrong email: ', url)

#2
import re
import json

with open('parsed_nginx.txt', 'w', encoding='utf-8') as fp:
    parsing = []
    with open('nginx_logs.txt') as f:
        for line in f:
            parsing += re.findall(
                r'^(?P<remote_addr>[^&]+) - - \[(?P<request_datetime>[^&]+)\] \"(?P<request_type>[^&]+) (?P<requested_resource>[^&]+) HTTP\/1.1\" (?P<response_code>[\d]+) (?P<response_size>[\d]+)[^&]+$',
                line)
    json.dump(parsing, fp)

#3
from functools import wraps

def type_logger(func):
    @wraps(func)
    def t_logger(*args, **kwargs):
        result =''
        for num in args:
            result += f'calc_cube({num} : {type(num)}, Результат ={func(num)},{type(func(num))}), '
        print(result)
        for key, val in kwargs.items():
            print(f'{func.__name__}({str(val)} : {type(val)}, Результат = {func(val)})')
    return t_logger

@type_logger
def calc_cube(x):
      return x ** 3

a = calc_cube(num1=5, num2=23.6)
b = calc_cube(25.3, 5, 2.0)
c = calc_cube(1)
print(calc_cube.__name__)
print(calc_cube.__doc__)

#4 декоратор, позволяющий валидировать входные значения функции и выбрасывать исключение ValueError
from functools import wraps
def val_checker(lam_func):
    def v_checker(calc_func):
        @wraps(calc_func)
        def _v_checker(num):
            if lam_func(num):
                return f'Куб {num} = {calc_func(num)}'
            else:
                raise ValueError('ValueError: wrong val', num)
        return _v_checker
    return v_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
b = calc_cube(2)

print(a, b)
