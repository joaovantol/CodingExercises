properDivisors <- function(n) {
    if (n == 1) return(0)
    
    divisors <- c(1)

    if (n == 2) return(divisors)

    for (i in 2:sqrt(n)) {
        if (n %% i == 0) {
            divisors <- c(divisors, i)
            if (i != n / i) {
                divisors <- c(divisors, n / i)
            }
        }
    }

    return(divisors)
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

