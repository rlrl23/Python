import sys

def add_sale(argv):
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(argv.pop())
        f.write('\n')

add_sale(sys.argv)