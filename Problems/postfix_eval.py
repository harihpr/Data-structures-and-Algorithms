exp = "17 10 + 3 * 9 /"
exp = exp.split(" ")
opstack = []

for o in exp:
    if o not in "+-*/":
        opstack.append(int(o))
    else:
        op2 = opstack.pop()
        op1 = opstack.pop()
        if o == "+":
            res = op1 + op2
        elif o == "-":
            res = op1 - op2
        elif o == "*":
            res = op1 * op2
        else:
            res = op1 / float(op2)
        opstack.append(res)
        
print opstack.pop()