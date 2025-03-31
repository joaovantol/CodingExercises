randomStrategy <- function(nSims = 5000, nPrisoners = 100, limitDrawers = 50) {
    success <- rep(0, nSims)
    sim <- 1

    while (sim <= nSims) {
        nSuccess <- 0
        prisoner <- 1
        while (prisoner <= nPrisoners) {
            if (prisoner %in% sample(1:nPrisoners, limitDrawers)) nSuccess <- nSuccess + 1
            prisoner <- prisoner + 1
        }
        success[sim] <- nSuccess
        sim <- sim + 1
    }

    prob <- sum(success==nPrisoners)/nSims

    return(prob)
}

optimalStrategy <- function(nSims = 5000, nPrisoners = 100, limitDrawers = 50) {
    success <- rep(0, nSims)
    sim <- 1

    while (sim <= nSims) {
        drawers <- sample(1:nPrisoners)
        nSuccess <- 0
        prisoner <- 1
        while (prisoner <= nPrisoners) {
            nTry <- 1
            check <- prisoner
            while (nTry <= limitDrawers) {
                if (prisoner == drawers[check]) {
                    nSuccess <- nSuccess + 1
                    break
                } 
                check <- drawers[check]
                nTry <- nTry + 1
            }
            prisoner <- prisoner + 1
        }
        success[sim] <- nSuccess
        sim <- sim + 1
    }

    prob <- sum(success==nPrisoners)/nSims

    return(prob)
}
