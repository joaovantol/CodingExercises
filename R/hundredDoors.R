passingDoors <- function(nDoors = 100) {
    doors <- logical(nDoors)
    
    i <- 1
    while (i <= nDoors) {
        toggleIndex <- seq(i, nDoors, i)
        doors[toggleIndex] <- !doors[toggleIndex]
        i <- i + 1
    }

    return(which(doors))
}
