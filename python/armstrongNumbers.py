def isArmstrong(n):
    digits = [int(x) for x in str(n)]
    power = len(digits)
    return sum([x ** power for x in digits]) == n

isArmstrong(9)
isArmstrong(10)
isArmstrong(153)
isArmstrong(154)
"tesss"