exp = "A + B * C"
exp = "".join(exp.split(" "))
pdict = {"(":1, "+":2, "-":2, "*":3, "/":3}
opstack = []
result = []

for o in exp:
	if o in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
		result.append(o)
	else:
		if o == "(":
			opstack.append(o)
		elif o == ")":
			while opstack[-1] != "(":
				result.append(opstack.pop())
			opstack.pop()
		else:
			while len(opstack) != 0 and pdict[o] <= pdict[opstack[-1]]:
				result.append(opstack.pop())
			opstack.append(o)

while len(opstack) != 0:
	result.append(opstack.pop())
print " ".join(result)
