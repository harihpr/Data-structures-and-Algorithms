A = 'DS'
col = 0
i = len(A)

for a in A:
    val = ord(a) - 64
    col += 26**(i-1) * val
    i -= 1
    
print col