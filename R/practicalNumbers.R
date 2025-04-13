source("./R/Euler/21.R", encoding = "UTF-8")

isPracticalNumber <- function(n) {
    if (n == 1 | n == 2) return (TRUE)

    divisors <- properDivisors(n)
    sums <- c()

    if (length(divisors) > 1) {
        for (divisor in divisors) {
            sums <- union(sums, sums + divisor)
            sums <- union(sums, divisor)
        }
    }

    out <- sum(1:(n-1) %in% sums) == (n-1)

    return(out)
}

sumOfPracticalNumbers <- function(n = 10000) {
    result <- 0

    for (i in 1:n) {
        if (isPracticalNumber(i) == TRUE) {
            result <- result + i
        }
    }

    return(result)
}

