source("./R/Euler/07.R", encoding = "UTF-8")

quadraticForm <- function(n, a, b) n^2 + a*n + b

findCoef <- function() {
    primes <- generatePrimeList(1000)
    consecutivePrimes <- 0

    for (b in primes[2:length(primes)]) {
        for (a in seq(-b+2, b-2, 2)) {
            n <- 1
            while (checkIfPrime(quadraticForm(n,a,b))) n <- n + 1
            if (n > consecutivePrimes) {
                consecutivePrimes <- n
                coef <- c(a,b)
            }
        }
    }

    return (coef)
}

prodCoef <- function() prod(findCoef())
