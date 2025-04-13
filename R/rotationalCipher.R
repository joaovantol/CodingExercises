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

rotationalCipher("omg", 5)
rotationalCipher("c", 0)
rotationalCipher("Cool", 26)
rotationalCipher("The quick brown fox jumps over the lazy dog.", 13)
rotationalCipher("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", 13)
