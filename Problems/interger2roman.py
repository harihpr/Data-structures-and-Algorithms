integer = 2497
roman_dict = [{1:'I'},{4:'IV'},{5:'V'},{9:'IX'},{10:'X'},{40:'XL'},{50:'L'},{90:'XC'},{100:'C'},{400:'CD'},{500:'D'},{900:'CM'},{1000:'M'}]
roman = ''

while integer:
    num = roman_dict[-1]
    if integer >= num.keys()[0]:
        temp = num.keys()[0]
        roman += num.values()[0]
        integer = integer - temp
    else:
        roman_dict.pop()
        
print roman