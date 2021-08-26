lado1, lado2, lado3 = map(int, input().split())
Numeros = [lado1, lado2, lado3]
A = max(Numeros)
B = min(Numeros)
C = lado1+ lado2 + lado3 - A - B
if A >= B + C:
    print('Invalido')
else:
    if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Valido-Escaleno')
        if lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print('Valido-Equilatero')
        if lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado3 == lado1 and lado1 != lado2):
        print('Valido-Isoceles')
        if lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
            print('Retangulo: S')
        else:
            print('Retangulo: N')