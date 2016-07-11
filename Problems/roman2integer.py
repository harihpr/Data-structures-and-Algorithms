roman = 'MMCDXCVII'
roman_dict = [{'I':1},{'IV':4},{'V':5},{'IX':9},{'X':10},{'XL':40},{'L':50},{'XC':90},{'C':100},{'CD':400},{'D':500},{'CM':900},{'M':1000}]
integer = 0

while roman:
    num = roman_dict[-1]
    if roman[0] == num.keys()[0]:
        integer += num.values()[0]
        roman = roman[1:]
    elif roman[:2] == num.keys()[0]:
        integer += num.values()[0]
        roman = roman[2:]        
    else:
        roman_dict.pop()

print integer