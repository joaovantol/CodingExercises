sumSpiralDiag <- function(dim) {
    evenSpiral <- FALSE
    if (1 != dim%%2) {
        dim <- dim - 1
        evenSpiral <- TRUE
    }

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

    if (evenSpiral) soma <- soma + n

    return(soma)
}
