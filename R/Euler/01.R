mult <- c(3,5)
limit <- 1000

multiples <- function(mult, limit) {
    naturals <- seq(limit-1)
    multiples <- c()

    for (i in naturals) {
        check <- TRUE
        for (j in 1:length(mult)) {
            if (check){
                if (check_multiple(i,mult[j]) == TRUE) {
                    multiples <- cbind(multiples, i)
                    check <- FALSE
                }
            }
        }
    }

    return(sum(multiples))
}

check_multiple <- function(numerador, denominador){
    resto <- numerador%%denominador

    return(ifelse(resto == 0, TRUE, FALSE))
}