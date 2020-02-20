def somar (a,b):
    resultado = a + b
    if resultado > 40:
        return resultado
    else:
        return ('ops, só retorno valores acima de 40')
numero1 = int(input('digite o primeiro número '))
numero2 = int(input('digite o segundo número '))
soma = somar(numero1, numero2)
print(soma)