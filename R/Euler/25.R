source("./R/Euler/20.R", encoding = "UTF-8")

require(gmp)

findFibonacciNumber <- function(size = 1000){
    previousNum <- 1
    currentNum <- 1
    index <- 2
    newNumber <- 0

    while (nchar(as.character(newNumber)) < size) {
        newNumber <- bigAdd(previousNum, currentNum)
        previousNum <- currentNum
        currentNum <- newNumber
        index <- index + 1
    }

    return(index)
}

findFibonacciNumberGMP <- function(size = 1000){
    previousNum <- 1
    currentNum <- 1
    index <- 2
    newNumber <- 0

    while (nchar(as.character(newNumber)) < size) {
        newNumber <- as.bigz(previousNum + currentNum)
        previousNum <- currentNum
        currentNum <- newNumber
        index <- index + 1
    }

    return(index)
}