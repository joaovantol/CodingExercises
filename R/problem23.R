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

# Solution with matrix
getSumsMat <- function(n = 28111) {
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

# Faster solution with set
getSumsSet <- function(n = 28111) {
    abundants <- getAbundantNumbers(n)
    sums <- c(1:n)

    for (abundant in abundants) {
        sums <- setdiff(sums, abundants + abundant)
        abundants <- abundants[c(-1)]
    }

    return(sum(sums))
}

# Solution with boolean
getSumsBool <- function(n = 28111) {
    abundants <- getAbundantNumbers(n)
    len <- length(abundants)
    sums <- logical(n)

    i <- 1
    while (i <= length(abundants)) {
        j <- i
        maxAbundant <- tail(which(abundants <= (n - abundants[i])),1)
        if (length(maxAbundant) == 0) break
        
        while (j <= maxAbundant) {
            soma <- sum(abundants[c(i, j)])
            sums[soma] <- TRUE
            j <- j + 1
        }
        i <- i + 1
    }

    # sums <- sum(which(sums == TRUE))

    return(sum(which(sums == FALSE)))
}
