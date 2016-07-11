plist = "[ ] } { "
plist = "".join(plist.split(" "))
pdict = {"(":")", "{":"}", "[":"]", "<":">"}
s = []
balanced = True
for p in plist:
	# if len(s)==0 and p not in ")}]>":
	# 	s.append(p)
	if len(s)==0 and p in ")}]>":
		s.append(p)
		break
	else:
		if p in "({[<":
			s.append(p)
		elif pdict[s[-1]]==p:
			s.pop()
		else:
			break

print s
print "Perfect" if not len(s) else "Not so"
