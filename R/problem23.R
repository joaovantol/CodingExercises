source("./R/problem21.R", encoding = "UTF-8")

getAbundantNumbers <- function(n) {
    abundants <- c()

    for (i in 2:n) {
        soma <- sum(properDivisors(i))
        if (soma > i) {
            abundants <- c(abundants, i)
        } 
    }

    return(abundants)
}

getSums <- function(n = 28123) {
    abundants <- getAbundantNumbers(n)
    len <- length(abundants)
    sums <- matrix(0, nrow = len, ncol = len)

    i <- 1
    while (i <= length(abundants)) {
        j <- i
        maxAbundant <- tail(which(abundants <= (n - abundants[i])),1)

        if (length(maxAbundant) == 0) break
        
        while (j <= maxAbundant) {
            sums[i, j] <- sum(abundants[c(i, j)])
            j <- j + 1
        }
        i <- i + 1
    }

    sums <- unique(as.vector(sums))

    totalSum <- sum(1:n)

    return(totalSum - sum(sums))
}
