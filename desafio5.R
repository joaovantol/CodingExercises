even_div <- function(n) {
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

even_div(20)