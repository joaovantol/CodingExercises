checkPythagorean <- function(a,b,c) {
    return(ifelse(a^2 + b^2 == c^2, TRUE, FALSE))
}

searchABC <- function(sum) {
    hasTriplet <- FALSE

    for (a in 1:floor(sum/3)) {
        for (b in a:floor(sum/2)) {
            c <- sum - a - b
            if (checkPythagorean(a,b,c)) {
                hasTriplet <- TRUE
                break
            }
        }
        if (hasTriplet) break
    }

    if (hasTriplet == FALSE) return("There is no triplet")

    return(list(a=a,b=b,c=c,prod=a*b*c))
}

searchABC(1000)