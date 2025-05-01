def maxThrill(atms):
    n = len(atms)
    atmIndex = [0,0]
    maxThrill = 0

    for i in range(n):
        for j in range(i, n):
            thrill = atms[i] + atms[j]
            if i != j:
              thrill += abs(i-j)
            if thrill > maxThrill:
                maxThrill = thrill
                atmIndex[0] = i
                atmIndex[1] = j

    return maxThrill, atmIndex

def maxThrillOn(atms):
    n = len(atms)
    indexLeft = 0
    indexRight = n - 1

    for i in range(1, n):
      if (atms[i] - atms[indexLeft]) > (i - indexLeft):
        indexLeft = i

    for j in range(n-2, -1, -1):
      if (atms[j] - atms[indexRight]) > (indexRight - j):
        indexRight = j

    thrill = atms[indexLeft] + atms[indexRight] + indexRight - indexLeft

    return thrill, [indexLeft, indexRight]

maxThrill([3,1,3])
maxThrillOn([3,1,3])

maxThrill([2,3,4,5])
maxThrillOn([2,3,4,5])

maxThrill([10, 10, 11, 13, 7, 8, 9])
maxThrillOn([10, 10, 11, 13, 7, 8, 9])

maxThrill([2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8])
maxThrillOn([2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8])
