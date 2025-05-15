# Quinta potência dos dígitos de 0 a 9
fifth_powers = {str(d): d**5 for d in range(10)}

# Estimar um limite superior: 
# 6 dígitos: 6 * 9^5 = 354294 (a partir de 7 dígitos, o número mínimo já ultrapassa a soma possível)
upper_limit = 6 * (9 ** 5)

# Inicializar a lista de números que satisfazem a condição
valid_numbers = []

# Testar números de 10 até o limite estimado
for num in range(10, upper_limit + 1):
    digit_sum = sum(fifth_powers[d] for d in str(num))
    if num == digit_sum:
        valid_numbers.append(num)

# Exibir os resultados
print("Números encontrados:", valid_numbers)
print("Soma dos números:", sum(valid_numbers))
