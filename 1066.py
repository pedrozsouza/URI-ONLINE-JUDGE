impares = 0
pares = 0
positivos = 0
negativos = 0
for c in range(0,5):
    c = int(input())
    if c%2==0:
        pares += 1
    if c%2==1:
        impares += 1
    if c > 0:
        positivos += 1
    if c < 0:
        negativos += 1
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")