require(gmp)

powerDigitSum <- function(n) {
    number <- as.bigz(2^n)
    return(sum(as.numeric(unlist(strsplit(as.character(number),"")))))
}