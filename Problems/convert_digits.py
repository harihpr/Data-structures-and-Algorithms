import math

num = 1205
A = 0
B = 5
diff = B-A
rep = 1

while rep != 10**(int(math.log10(num))+1):
    temp = (num/rep)%10
    temp = diff*rep if temp==A else 0
    num += temp
    rep *= 10
    
print num