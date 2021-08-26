contador = 0
for c in range(0,5):
    c = int(input())
    if c%2==0:
        contador += 1
print(f"{contador} valores pares")