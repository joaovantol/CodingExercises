find_pal <- function(n) {
    inf <- 10^(n-1)
    sup <- 10^n-1
    prod <- c()

    while (sup > inf) {
        for (i in sup:inf) {
            for (j in sup:inf) {
                if (check_pal(i*j)) {
                    prod <- c(prod, i*j)
                    break
                }
            }
            if (check_pal(i*j)) {
                break
            }
        }
        sup <- i-1
        inf <- j
    }

    return(prod)
}

check_pal <- function(n) {
    word <- as.character(n)
    reverse <- paste(rev(unlist(strsplit(word, ""))), collapse = "")

    return(ifelse(word == reverse, TRUE, FALSE))
}

max(find_pal(3))