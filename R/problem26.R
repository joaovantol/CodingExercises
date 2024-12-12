getCycleLength <- function(n) {
    dividend <- 1
    remainders <- c(1)

    repeat {
        dividend <- (dividend * 10) %% n
        if (dividend == 0) return(0)
        if (dividend %in% remainders) break
        remainders <- c(remainders, dividend)
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