def newtonSqrt(number):
    if number == 0:
        return 0

    x = 1
    while True:
        xNew = (x + number / x) / 2
        if abs(x - xNew) < 1e-3:
            break
        x = xNew

    return int(x) 

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