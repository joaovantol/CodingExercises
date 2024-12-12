getCycleLength <- function(n) {
    remainder <- 1
    remainders <- c(remainder)

    repeat {
        remainder <- (remainder * 10) %% n
        if (remainder == 0) return(0)
        if (remainder %in% remainders) break
        remainders <- c(remainders, remainder)
    }

    return(length(remainders))
}

getDwithLongestCycle <- function(d = 1000) {
    lengths <- c(0)
    i <- 2

    while (i < d) {
        lengths <- c(lengths, getCycleLength(i))
        i <- i + 1
    }
    return(which.max(lengths))
}