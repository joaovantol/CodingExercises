function properDivisors(n::Int64)
    sequence = [1:1:n-1;]
    filter = (n .% sequence .== 0)

    return sequence[filter]
end

function getAbundantNumbers(n::Int64)
    abundants = []

    for i in 2:n
        soma = sum(properDivisors(i))
            if soma > i
                abundants = append!(abundants, i)
            end
    end

    return abundants
end

# Solution with matrix
function getSumsMat(n::Int64=28111)
    abundants = getAbundantNumbers(n)
    len = length(abundants)
    sums = zeros(len, len)

    i = 1
    while i <= len
        j = i
        maxAbundant = findfirst(x -> x > (n - abundants[i]), abundants) - 1
        while j <= maxAbundant
            sums[i, j] = sum(abundants[[i,j]])
            j = j + 1
        end
        i = i + 1
    end

    sums = unique(sums)
    totalSum = sum([1:1:n;])

    return(totalSum - sum(sums))
end

# Faster solution with set
function getSumsSet(n::Int64=28111)
    abundants = getAbundantNumbers(n)
    sums = Set(1:n)

    for abundant in abundants
        setdiff!(sums, abundants .+ abundant)
        abundants = abundants[2:length(abundants)]
    end

    return(sum(sums))
end