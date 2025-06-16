def powersSum(power):
    powers = {str(digit): digit**power for digit in range(10)}

    digits = 1
    minValue = 10**(digits-1)
    maxSum = powers["9"]

    while minValue < maxSum:
        digits += 1
        minValue = 10**(digits-1)
        maxSum = powers["9"]*digits

    maxValue = (digits-1)*powers["9"]

    validNumbers = []

    for num in range(10, maxValue + 1):
        powersSum = sum(powers[digit] for digit in str(num))
        if num == powersSum:
            validNumbers.append(num)

    return validNumbers, sum(validNumbers)
