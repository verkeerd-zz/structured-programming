symbol = '*'

while True:
    try:
        length = int(input('Hoe groot moet de piramide zijn? '))
        break
    except ValueError:
        length = print('Je moet een getal geven.')

print('Met twee for loops een linkszijdige pyramide:')
for i in range(1, length):
    print(symbol * i)
for i in range(length):
    print(symbol * (length - i))

print('\nmet twee while loops een linkszijdige pyramide:')
count = 1

while count != length:
    print(symbol * count)
    count += 1

while count != 0:
    print(symbol * count)
    count -= 1

print('Met twee for loops een rechtszijdige pyramide:')
for i in range(1, length):
    print(' ' * (length - i) + symbol * i)

for i in range(length):
    print(' ' * i + symbol * (length - i))


count = 1

print('Met twee while loops een rechtszijdige pyramide:')
while count != length:
    print(' ' * (length - count) + symbol * count)
    count += 1

while count != 0:
    print(' ' * (length - count) + symbol * count)
    count -= 1

