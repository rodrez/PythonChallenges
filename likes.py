def likes(names):
    if len(names) == 0:
        print('no one like this')
    elif len(names) == 1:
        print(f'{names[0]} like this')
    elif len(names) == 2:
        print(f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        print(f'{names[0]}, {names[1]} and {names[2]} like this')
    else:
        print(f'{names[0]}, {na
