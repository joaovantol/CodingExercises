isLuhnValid <- function(string) {
    string <- gsub(" ", "", string)
    if (1 == nchar(string)) return("invalid input")

    chars <- unlist(strsplit(string, ""))
    if (!all(chars %in% c("1","2","3","4","5","6","7","8","9","0"))) 
        return("invalid input")

    digits <- as.numeric(chars)
    index <- rev(seq(length(digits)-1, 1, -2))
    doubles <- digits[index]*2
    doubles[doubles > 9] <- doubles[doubles > 9] - 9
    digits[index] <- doubles

    return(sum(digits) %% 10 == 0)
}

isLuhnValid("4539 3195 0343 6467")
isLuhnValid("8273 1232 7352 0569")
isLuhnValid("45a9 3195 0343 6467")
isLuhnValid("4")
isLuhnValid("16")
isLuhnValid("26")
isLuhnValid("026")
isLuhnValid("326")
