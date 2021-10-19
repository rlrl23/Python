#Вывести курс к рублю по коду валюты, полученный с сайта
import requests
from decimal import Decimal

def currency_rates(char_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response.content
    response.encoding = 'utf-8'
    ind_char_code= response.text.find(char_code.upper())
    first_ind_value=response.text.find('Value', ind_char_code) +6
    last_ind_value= response.text.find('Value', first_ind_value) -2
    value= response.text[first_ind_value:last_ind_value]
    value= value.replace(',', '.')
    print(Decimal(value))
    print(response.headers['Date'])

if __name__=='__main__':
    currency_rates('eur')
    currency_rates('USD')