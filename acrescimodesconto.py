def percentual(valor,porcentagem):
    return valor *(porcentagem / 100)
preco = float(input())
valor_percentual = float(input())
preco_acres = preco + percentual(preco,valor_percentual)
preco_desc = preco - percentual(preco,valor_percentual)
print("%.2f" % preco_acres)
print("%.2f" % preco_desc)
