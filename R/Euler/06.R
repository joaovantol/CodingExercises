sumOfSquares <- function(n) {
    return(sum((1:n)^2))
}

squareOfSum <- function(n) {
    return(sum(1:n)^2)
}

difference <- function(n) {
    return(squareOfSum(n) - sumOfSquares(n))
}

difference(100)