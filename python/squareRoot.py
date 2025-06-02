def newtonSqrt(number):
    if number == 0:
        return 0

    guess = number
    while True:
        nextGuess = (guess + number / guess) / 2
        if abs(guess - nextGuess) < 1e-10:
            break
        guess = nextGuess

    return int(guess) 

def binSqrt(number):
    if number < 2:
        return number

    low, high = 1, number // 2

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            low = mid + 1
        else:
            high = mid - 1

    return high