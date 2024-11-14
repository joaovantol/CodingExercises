readNames <- function() {
    names <- readLines("./0022_names.txt", warn = FALSE)
    names <- unlist(strsplit(names, ","))
    names <- gsub("[[:punct:]]", "", names)
    names <- sort(names)
}

nameValue <- function(name) {
    letterVec <- unlist(strsplit(name,""))
    value <- 0
    
    for (i in 1:length(letterVec)) {
        value <- value + letterValue(letterVec[i])
    }

    return(value)
}

letterValue <- function(letter) which(LETTERS == letter)

totalScore <- function() {
    list <- readNames()
    score <- 0

    for (i in 1:length(list)) {
        alphaScore <- nameValue(list[i])
        nameScore <- alphaScore * i
        score <- score + nameScore
    }

    return(score)
}
