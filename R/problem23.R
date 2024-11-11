source("./R/problem21.R", encoding = "UTF-8")

getAbundantNumbers <- function(n) {
    abundants <- c()

    for (i in 2:n) {
        soma <- sum(properDivisors(i))
        if (soma > i) {
            abundants <- c(abundants, i)
        } 
    }

    return(abundants)
}

# getSums <- function(n) {
#     abundants <- getAbundantNumbers(n)
#     numbers <- c()

#     i <- 1
#     while (i <= length(abundants)) {
#         j <- i
#         while (j <= length(abundants)) {
#             newNumber <- abundants[i] + abundants[j]
#             if (newNumber <= 300 & !newNumber %in% numbers) {
#                 numbers <- c(numbers, newNumber)
#             }
#             j <- j + 1
#         }
#         i <- i + 1
#     }

#     return(numbers)
# }

# getSums2 <- function() {
#     abundants <- getAbundantNumbers()
#     numbers <- c()

#     i <- 1
#     while (i <= length(abundants)) {
#         print(i)
#         j <- i
#         while (j <= length(abundants)) {
#             newNumbers <- abundants[i] + abundants[which(abundants <= 28110 - abundants[i])]
#             numbers <- c(numbers, newNumbers[!newNumbers %in% numbers]) 
#             j <- j + 1
#         }
#         i <- i + 1
#     }

#     return(numbers)
# }

# # ab1 <- ab[1] + ab[which(ab <= 300 - ab[1])]
# # ab2 <- ab[2] + ab[which(ab <= 300 - ab[2])]
# # ab1 <- c(ab1, ab2[!ab2 %in% ab1])

# checkSums <- function(n) {
#     abundants <- getAbundantNumbers(n)
#     minAbundant <- head(abundants,1)
#     maxAbundant <- tail(abundants,1)
#     numbers <- 1:23

#     i <- 25
#     while (i <= (minAbundant + maxAbundant)) {

#     }
# }


# # calculate the sum of those sums of the abundant numbers
# len <- length(num.abundant)
# sums <- matrix(0, nrow = len, ncol = len)
# for (i in 1:len) {
#   for (j in i:len) {
#     sums[i, j] <- sum(num.abundant[c(i, j)])
#   }
# }
# sums <- unique(as.vector(sums))
# sums <- sums[sums <= 28123]
# result <- sum(num.lst) - sum(sums)
# cat("The result is:", result, "\n")

getSums <- function(n) {
    abundants <- getAbundantNumbers(n)
    len <- length(abundants)
    sums <- matrix(0, nrow = len, ncol = len)

    i <- 1
    while (i <= length(abundants)) {
        j <- i
        while (j <= length(abundants)) {
            sums[i, j] <- sum(abundants[c(i, j)])
            j <- j + 1
        }
        i <- i + 1
    }

    sums <- unique(as.vector(sums))
    sums <- sums[sums <= 28123]

    totalSum <- sum(1:n)

    return(totalSum - sum(sums))
}

