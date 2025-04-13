generateTriangleSeq <- function(n, search = FALSE, ndiv = 0, primes) {
    sequence <- c(1)
    naturals <- 2:n

    for (i in 2:n) {
        new <- tail(sequence, 1) + i

            if (search) {
                if (nFactors(new, primes) > ndiv) return(new)
            }

        sequence <- c(sequence, new)
    }

    return(sequence)
}

nDivisors <- function(n) {
    return(sum(n%%(1:n)==0))
}

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

nFactors <- function(x, prime = prime) {
    m <- length(prime)
    fac.count <- numeric(m)
    for (i in 1:m) {
        while (x%%prime[i] == 0) {
            fac.count[i] <- fac.count[i] + 1
            x = x/prime[i]
        }
        while (x == 1) break
    }
    return(prod(fac.count + 1))
}

primes <- generatePrimeList(100)

generateTriangleSeq(10e9, TRUE, 500, primes)