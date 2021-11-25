x, y = int(input('красных: ')), int(input('белых: '))
x1, y1, result = x, y, ''
if x > y:
    if x / y > 2:
        print('Нет решения')
    else:
        while x1 + y1 > 0:
            if x1 > y1:
                result += 'RWR'
                x1 -= 2
                y1 -= 1
            else:
                result += 'RW'
                x1 -= 1
                y1 -= 1
        print(result)
elif x < y:
    if y / x > 2:
        print('Нет решения')
    else:
        while x1 + y1 > 0:
            if x1 < y1:
                result += 'WRW'
                x1 -= 1
                y1 -= 2
            else:
                result += 'WR'
                x1 -= 1
                y1 -= 1
        print(result)
else:
    print('можно')
    for i in range(x):
        result += 'RW'
    print(result)
