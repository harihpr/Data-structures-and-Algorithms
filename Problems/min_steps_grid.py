X = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
Y = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
if type(X)==list and type(Y)==list:
    lst = []
    for i in range(len(X)):
        lst.append([X[i], Y[i]])
    
    origin = lst[0]
    steps = 0
    for i in range(1, len(lst)):
        while origin != lst[i]:
            temp = min( abs(lst[i][0]-origin[0]), abs(lst[i][1]-origin[1]))
            if origin[0]==lst[i][0]:
                temp = abs(lst[i][1] - origin[1])
                origin = lst[i]
            elif origin[1]==lst[i][1]:
                temp = abs(lst[i][0] - origin[0])
                origin = lst[i]
            elif lst[i][0]>origin[0] and lst[i][1]>origin[1]:
                origin[0] += temp
                origin[1] += temp
            elif lst[i][0]>origin[0] and lst[i][1]<origin[1]:
                origin[0] += temp
                origin[1] -= temp
            elif lst[i][0]<origin[0] and lst[i][1]<origin[1]:
                origin[0] -= temp
                origin[1] -= temp
            else:
                origin[0] -= temp
                origin[1] += temp
            steps += temp
    print steps
else:
    print 0