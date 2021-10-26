import sys

def show_sales(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        num = 1
        num_line={}
        for line in f:
            num_line[num] = line.replace('\n','')
            num+=1
    if len(argv)> 2:
        for i in range(int(argv[1]), int(argv[2])+1):
            print(num_line[i])
    elif len(argv)>1:
        for i in range(int(argv[1]), len(num_line)+1):
            print(num_line[i])
    else:
        for i in range(1, len(num_line) + 1):
            print(num_line[i])

show_sales(sys.argv)

