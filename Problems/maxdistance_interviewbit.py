A = [-1,-1,2]
s = [b[0]+1 for b in sorted(enumerate(A), key=lambda i:i[1])]
print A
print s

mini = s[0]
diff = 0

for i in range(1,len(s)):
    print s[i], mini
    if s[i]-mini>=0 and s[i]-mini>=diff:
        diff = s[i]-mini
    if s[i]<mini:
        mini = s[i]
    
    print diff