A = 8
row = [1]

for i in range(1,A+1):
    row.append(row[i-1]*(A+1-i)/i)
    
print row