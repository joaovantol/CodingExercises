generatePrimeList <- function(number) {
    if (number == 2) return(2)

    lista <- c(2, seq(from=3, to=number, by=2))
    primo <- 2

    i <- 1

    while (primo^2 < number) {
        lista <- lista[lista == primo | lista %% primo != 0]
        i <- i + 1
        primo <- lista[i]
    }

    return(lista)
}

checkIfPrime <- function(n) {
    if (n < 2) return(FALSE)
    
    primes <- generatePrimeList(ceiling(sqrt(n)))
    isPrime <- prod(n%%primes != 0) == 1

    return(isPrime)
}

findNthPrime <- function(n) {
    i <- 2
    ord <- 1

    while (ord < n) {
        i <- i + 1
        if (checkIfPrime(i)) {
            ord <- ord + 1
            i <- i + 1
        }
    }

    return(i - 1)
}

findNthPrime(10001)