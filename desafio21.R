proper_divisors <- function(n) {
    if (n == 1) {
        return(0)
    }
    
    sequence <- 1:(n-1)
    filter <- (n %% sequence) == 0

    return(sequence[filter])
}

is_amicable <- function(a, b) {
    return(a == sum(proper_divisors(b)) & a != b)
}

sum_amicable_numbers <- function(limit) {
    numbers <- c()
    sums <- c()

    for (i in 2:limit) {
        if (!i %in% sums) {
            soma <- sum(proper_divisors(i))

            if (soma > i & soma < limit) {
                sums <- c(sums, soma)
            }

            if (is_amicable(i, soma)) {
                numbers <- c(numbers, soma, i)
            }
        } 
    }

    return(sum(numbers))
}

