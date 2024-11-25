require(gmp)

bigAdd <- function(a, b) {
  if (nchar(a)<nchar(b)) 
    a <- paste0(paste(rep(0, nchar(b) - nchar(a)), collapse = ""), a)
  if (nchar(a)>nchar(b)) 
    b <- paste0(paste(rep(0, nchar(a) - nchar(b)), collapse = ""), b)
  solution <- vector()
  remainder <- 0
  for (i in nchar(b):1) {
    p <- as.numeric(substr(a, i, i))
    q <- as.numeric(substr(b, i, i))
    r <- p + q + remainder
    if (r >= 10 & i != 1) {
      solution <- c(solution, r %% 10)
      remainder <- (r - (r %% 10)) / 10
    } else {
      solution <- c(solution, r)
      remainder <- 0
    }
  }
  return(paste(rev(solution), collapse = ""))
}

findFibonacciNumber <- function(size){
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

findFibonacciNumberGMP <- function(size){
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