A = 9
if A<1:
    print 'Not possible'
elif A==1:
    print [[1]]
elif A==2:
    print [[1],[1,1]]
else:
    tri = [[1],[1,1]]
    for i in range(3,A+1):
        row = [1]
        for j in range(1,len(tri[-1])):
            row.append(tri[-1][j]+tri[-1][j-1])
        row.append(1)
        tri.append(row)
    print tri