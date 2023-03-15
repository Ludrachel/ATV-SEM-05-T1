def inverter(numero):
    unidade = numero % 10
    numero = numero // 10
    dezena = numero % 10
    numero = numero // 10
    centena = numero % 10
    numero = numero // 10
    milhar = numero % 10
    numero_invertido = (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar
    return numero_invertido
n = int(input())
print(f'{inverter(n)}')
