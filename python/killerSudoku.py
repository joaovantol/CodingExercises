from itertools import combinations
        
def killerSudoku(sumValue, cageSize, restrictions = []):
    validDigits = [d for d in range(1, 10) if d not in restrictions]
    validCombinations = [
        combination for combination in combinations(validDigits, cageSize) if
        sum(combination) == sumValue]

    return validCombinations
    

killerSudoku(7, 3)
killerSudoku(10, 2)
killerSudoku(10, 2, [1,4])

