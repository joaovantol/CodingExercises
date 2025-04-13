desafio2 <- function(){
    fibonacci <- c(1,2)

    while (tail(fibonacci, 1) < 4000000){
        fibonacci[length(fibonacci) + 1] <- sum(tail(fibonacci,2))
    }

    terms <- fibonacci[(!fibonacci%%2) & (fibonacci < 4000000)]

    return(sum(terms))
}