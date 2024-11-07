proper_divisors <- function(n) {
    if (n == 1) {
        return(0)
    }
    
    sequence <- 1:(n-1)
    filter <- (n %% sequence) == 0

    return(sequence[filter])
}

sum_amicable_numbers <- function(limit) {
    numbers <- c()
    sums <- c()

    for (i in 2:limit) {
        if (!i %in% sums) {
            soma <- sum(proper_divisors(i))

            if (soma > i) {
            sums <- c(sums, soma)
            }

            is_amicable <- i == sum(proper_divisors(soma)) & i != soma

            if (is_amicable) {
                numbers <- c(numbers, soma, i)

            }
        } 
    }

    return(sum(numbers))
}

# sum(amicable_numbers(10000))