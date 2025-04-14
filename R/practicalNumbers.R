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

sumOfPracticals <- function(n = 10000) {
    result <- 0

    i <- 1
    while (i <= n) {
        if (isPracticalNumber(i)) {
            result <- result + i
        }
        i <- i + 1
    }

    return(result)
}

