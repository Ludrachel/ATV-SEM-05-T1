def min_para_hrs(qtd_minutos):
    horas = qtd_minutos // 60
    minutos = qtd_minutos % 60
    return f'{horas}:{minutos}'
minutos = int(input())
horas = min_para_hrs(minutos)
print(f'{horas}')
