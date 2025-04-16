isArmstrong <- function(n) {
    nString <- as.character(n)
    nChars <- unlist(strsplit(nString, ""))
    digits <- as.numeric(nChars)
    power <- length(digits)

    return(sum(digits^power) == n)
}

isArmstrong(9)
isArmstrong(10)
isArmstrong(153)
isArmstrong(154)
