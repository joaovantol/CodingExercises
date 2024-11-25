lexicographicOrder <- function(nums = c(0,1,2,3,4,5,6,7,8,9), posit = 1e6) {

    numbers <- sort(nums)
    len <- length(nums)
    order <- c()

    while (len > 0) {
        index <- ceiling(posit / (factorial(len) / len))
        if (index > len) return(
            "posição n maior do que o número total de permutações")
        
        order <- c(order, numbers[index])
        numbers <- numbers[-c(index)]
        posit <- posit - (factorial(len) / len * (index - 1))
        len <- length(numbers)
    }

    return(Reduce(paste0, order))
}