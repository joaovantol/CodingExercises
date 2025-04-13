prime_factors <- function(number) {
    factors <- c()
    primes <- generate_prime_list(floor(sqrt(number)))
    div_index <- which(number %% primes == 0)

    if (length(div_index) == 0) {
        return(number)
    }

    for (divisor in primes[div_index]) {
        while (number %% divisor == 0) {
            factors <- c(factors, divisor)
            number <- number / divisor
        }
    }

    if (number > 1) factors <- c(factors, number)

    return(factors)

}

generate_prime_list <- function(number) {
    lista <- 2:number
    primo <- 2

    i <- 1

    while (primo^2 < number) {
        lista <- lista[lista == primo | lista %% primo != 0]
        i <- i + 1
        primo <- lista[i]
    }

    return(lista)
}

max(prime_factors(600851475143))

