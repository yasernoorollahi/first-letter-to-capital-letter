def solve(s):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = s.split(' ')
    for i in range(len(l)):
        if l[i].startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            flag = False
            if not flag:
                for j in range(len(l[i])):
                    if l[i][j] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                        flag = True
                        c = str(l[i][j].upper())
                        tt = l[i].replace(l[i][j], c)
                        l[i] = tt
                        break
        else:
            l[i] = l[i].capitalize()

    laststr = ' '.join(l)
    return laststr


dd1 = solve('q w e r t y u i o pass d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  KLZ X C V B N M')
dd2 = solve('1 w 2 r 3g')
dd2 = solve('1w 2r 3grate  this3numbers 4internet')
print(dd1)
print(dd2)
