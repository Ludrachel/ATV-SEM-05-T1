#escreva um programa que ler três valores inteiros(a,b,c).calcule e mostre o resultado da função
a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))
c = int(input("digite o valor de c:"))
def calcular(a,b,c):
    return 2 * a + 5 * b - c
def resultado():
    print(f'o resultado é:'{calcular(a,b,c)})
resultado()
