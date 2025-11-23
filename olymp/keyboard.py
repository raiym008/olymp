keyboard = [
    'q', 'w', 'e', 'r', 't', 
    'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'z',
    'x', 'c', 'v', 'b', 'n',
    'm'
    ]

l = input()
for i in range(len(keyboard)):
    if l == 'm':
        print('q')
        break

    if keyboard[i] == l:
        print(keyboard[i+1])