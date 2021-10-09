#Реализовать склонение слова «процент» во фразе «N процентов»
for percent in range(1, 101):
    if percent == 11 or percent == 12 or percent == 13 or percent == 14:
        print(percent, 'процентов')
    elif percent ==1 or percent %10 ==1:
        print (percent, 'процент')
    elif percent % 10 >1 and percent % 10 <5:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
