# a matriz dos caminhos tem dimensões aumentadas em 1
ncaminhos <- function(dim) {
    dims <- as.numeric(unlist(strsplit(dim, "x")))
    horiz <- dims[1] + 1
    vert <- dims[2] + 1

    matriz <- matrix(ncol = horiz, nrow = vert)
    matriz[vert, -horiz] <- 1
    matriz[-vert, horiz] <- 1

    for (i in (vert-1):1) {
        for (j in (horiz-1):1) {
            matriz[i,j] <- matriz[i+1,j] + matriz[i,j+1]
        }
    }

    return(matriz[1,1])
}

ncaminhos("20x20")