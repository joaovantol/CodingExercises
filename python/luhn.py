def isLuhnValid(string):
    string = string.replace(" ", "")
    
    if len(string) == 1:
        return "invalid input"
    if not all(x.isdigit() for x in string):
        return "invalid input"
    
    digits = [int(x) for x in string]
    
    for i in range(len(digits) - 2, -1, -2):
        print(i)
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    return sum(digits) % 10 == 0

isLuhnValid("4539 3195 0343 6467")
isLuhnValid("8273 1232 7352 0569")
isLuhnValid("45a9 3195 0343 6467")
isLuhnValid("4")
isLuhnValid("16")
isLuhnValid("26")
isLuhnValid("026")
isLuhnValid("326")