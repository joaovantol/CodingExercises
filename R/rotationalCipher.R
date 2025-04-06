rotationalCipher <- function(string, rot) {
    letras <- c(letters, letters)
    LETRAS <- c(LETTERS, LETTERS)
    caracteres <- unlist(strsplit(string, ""))
    cipher <- c()
    for (caracter in caracteres) {
        if (caracter %in% letras) {
            caracter <- letras[which(caracter == letras)[1] + rot]
        }
        if (caracter %in% LETRAS) {
            caracter <- LETRAS[which(caracter == LETRAS)[1] + rot]
        }
        cipher <- c(cipher, caracter)
    }
    return(paste(cipher, collapse = ""))
}
