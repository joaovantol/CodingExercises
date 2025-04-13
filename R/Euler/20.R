require(gmp)

# solution using gmp library
fatDigitSumGMP <- function(n) {
    fat <- factorialZ(n)
    sum <- sum(as.numeric(unlist(strsplit(as.character(fat), ""))))

    return(sum)
}

# solution using strings
bigAdd <- function(a, b) {
  ## Add leading zeros to smallest number
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

bigFactorial <- function(x) {
    x <- floor(x)
    bf <- 1
    if (x > 1) {
        for (i in 2:x) {
            bf <- Reduce(bigAdd, rep(bf,i))
        }
    }
    return (bf)
}

fatDigitSumString <- function(n) {
    fat <- bigFactorial(n)
    sum <- sum(as.numeric(unlist(strsplit(as.character(fat), ""))))

    return(sum)
}
