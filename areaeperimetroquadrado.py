def area_quadrado(lado):
    return lado * lado
def perimetro_quadrado(lado):
    return lado * 4
valor_lado = float(input())
print("%10.4f" % area_quadrado(valor_lado))
print("%10.4f" % perimetro_quadrado(valor_lado))
