require(stringi)

cryptoSquare <- function(string) {
    normalized <- gsub("[[:space:][:punct:]]", "", tolower(string))
    normalized <- stri_trans_general(normalized, "Latin-ASCII")

    r <- floor(sqrt(nchar(normalized)))
    if (r*r == nchar(normalized)) {
        c <- r
    } else if (r*(r+1) >= nchar(normalized)) {
        c <- r + 1
    } else {
        r <- r + 1
        c <- r
    }

    messageLength <- c*r

    while (messageLength > nchar(normalized)) {
        normalized <- paste(normalized, "", collapse = "")
    }

    characters <- unlist(strsplit(normalized, ""))
    codedChars <- c()
    for (column in seq(1:c)) {
        for (linha in seq(1:r)) {
            codedChars <- c(codedChars, characters[column+(linha-1)*c])
        }
    }    

    finalCode <- c()
    while (length(codedChars) >= r) {
        finalCode <- c(finalCode, paste(codedChars[1:r], collapse = ""))
        codedChars <- codedChars[(r+1):length(codedChars)]
    }

    return(paste(finalCode, collapse = " "))
}

cryptoSquare("If man was meant to stay on the ground, god would have given us roots.")
cryptoSquare("Essa frase é bem aleatória, feita apenas de brincadeira para testar este exercício")

#