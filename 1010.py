codigo,numero,valor = map(float,input().split())
codigo2,numero2,valor2 = map(float,input().split())

soma = (numero * valor) + (numero2 * valor2)
print(f"VALOR A PAGAR: R$ {soma}")