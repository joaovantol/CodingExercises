collatz <- function(n, earlyBreak = FALSE) {
    sequence <- c(n)
    nEarlyBreak <- n

    while (n != 1) {
        n <- ifelse(n %% 2 == 0, n/2, 3*n + 1)
        if (n < nEarlyBreak & earlyBreak) break
        sequence <- c(sequence, n)
    }
    return(sequence)
}

searchLargestCollatz <- function(maxNumber) {
    maxLength <- 1
    maxLengthTotal <- 1
    i <- 1
    answer <- 1

    while (i<maxNumber) {
        print(i)
        sequence <- collatz(i+1, earlyBreak = TRUE)
        len <- length(sequence)
        
        if (len > maxLength) {
            maxLength <- len
            lenTotal <- length(collatz(i+1))
            if (lenTotal > maxLengthTotal) {
                maxLengthTotal <- lenTotal
                answer <- i+1
            }
        } 

        i <- i+1
    }
    return(answer)
}

searchLargestCollatz <- function(maxNumber) {
    i <- 1
    answer <- 1

    while (i<maxNumber) {
        print(i)



        i <- i+1
    }
    return(answer)
}

lens <- c()
i <- 1
while (i<1e6) {
    lens <- c(lens, length(collatz(i)))
    i <- i + 1
    print(i)
}

lens <- c()
for (i in 1:1e6) {
    lens <- c(lens, length(collatz(i)))
}

which(lens == max(lens)) #837799

searchLargestCollatz <- function(maxNumber) {
    lens <- c()
    i <- 1

    while (i<=maxNumber) {
        print(i)
        sequence <- collatz(i, earlyBreak = TRUE)
        if (tail(sequence,1) == 1) {
            lens <- c(lens, length(sequence))
        } else {
            len <- length(sequence)
            lens <- c(lens, (length(sequence) + lens[tail(sequence,1)/2]))
        }
        i <- i+1
    }
    return(which(lens==max(lens)))
}


searchLargestCollatz <- function(maxNumber) {
    maxLength <- length(collatz(maxNumber))
    i <- maxNumber
    answer <- 1

    while (i>1) {
        print(i)
        len <- length(collatz(i-1))
        if (len > maxLength) {
            maxLength <- len
            answer <- i-1
        }
        i <- i-1
    }
    return(answer)
}

################### Melhor resposta: 2min 40s
collatzSize <- function(n) {
    size <- 1

    while (n != 1) {
        n <- ifelse(n %% 2 == 0, n/2, 3*n + 1)
        size <- size+1
    }

    return(size)
}

searchLargestCollatz <- function(maxNumber) {
    maxLength <- 1
    i <- 1
    answer <- 1

    while (i<maxNumber) {
        # print(i)
        len <- collatzSize(i+1)
        if (len > maxLength) {
            maxLength <- len
            answer <- i+1
        }
        i <- i+1
    }
    return(answer)
}

searchLargestCollatz(1e6)