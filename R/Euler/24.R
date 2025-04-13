nthPermutation <- function(digits = c(0,1,2,3,4,5,6,7,8,9), position = 1e6) {
    digits <- sort(digits)
    len <- length(digits)
    answer <- c()

    while (len > 0) {
        partitionSize <- factorial(len) / len
        index <- ceiling(position / partitionSize)
        if (index > len) return("position greater than number of permutations")
        answer <- c(answer, digits[index])
        digits <- digits[-c(index)]
        position <- position - partitionSize * (index - 1)
        len <- length(digits)
    }

    return(Reduce(paste0, answer))
}