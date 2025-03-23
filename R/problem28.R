sumSpiralDiag <- function(dim) {
    if (dim%%2 != 1) return("Invalid dimension for a spiral")
    if (dim == 1) return(1)

    nTurns <- (dim - 1) / 2
    soma <- turn <- 1
    n <- 3
    step <- 2

    while (turn <= nTurns) {
        soma <- soma + 4*n + 6*step
        n <- n + 4*step + 2
        step <- step + 2
        turn <- turn + 1
    }

    return(soma)
}
