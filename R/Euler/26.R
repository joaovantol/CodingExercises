getCycleLength <- function(n) {
    remainder <- 1
    remainders <- c(remainder)

    repeat {
        remainder <- (remainder * 10) %% n
        if (remainder == 0) return(0)
        if (remainder %in% remainders) break
        remainders <- c(remainders, remainder)
    }

    return(length(remainders) - which(remainders == remainder) + 1)
}

getDwithLongestCycle <- function(d = 999) {
    maxLength <- 0
    i <- d

    while (i > 1) {
        if (i < maxLength) break
        length <- getCycleLength(i)
        if (length > maxLength) {
            maxLength <- length
            answer <- i
        }
        i <- i - 1
    }

    return(answer)
}
