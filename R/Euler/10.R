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

sum(generatePrimeList(2000000))