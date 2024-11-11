properDivisors <- function(n) {
    if (n == 1) {
        return(0)
    }
    
    sequence <- 1:(n-1)
    filter <- (n %% sequence) == 0

    return(sequence[filter])
}

isAmicable <- function(a, b) {
    return(a == sum(properDivisors(b)) & a != b)
}

sumAmicableNumbers <- function(limit) {
    numbers <- c()
    sums <- c()

    for (i in 2:limit) {
        if (!i %in% sums) {
            soma <- sum(properDivisors(i))

            if (soma > i & soma < limit) {
                sums <- c(sums, soma)
            }

            if (isAmicable(i, soma)) {
                numbers <- c(numbers, soma, i)
            }
        } 
    }

    return(sum(numbers))
}

