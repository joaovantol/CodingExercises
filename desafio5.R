even_div <- function(n) {
    div <- 4:n
    i <- 6  # 6 é divisível por 1, 2 e 3. Resta encontrar um número
            # que também é divisível por 4 e assim por diante

    for (divs in div) {
        j <- i
        while (sum(i%%(1:divs)) != 0) {
            i <- i + j
        }
    }

    return(i)
}

even_div(20)

even_div2 <- function(n) {
    divs <- 1:n
    i <- 1 

    for (div in divs) {
        j <- i
        while (sum(i%%(1:div)) != 0) {
            i <- i + j
        }
    }

    return(i)
}