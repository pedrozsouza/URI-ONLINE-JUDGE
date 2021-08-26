contador = 0
media = 0
somatorio = 0
for c in range(0,6):
    c = float(input())
    if c > 0:
        contador += 1
        somatorio += c
media = somatorio / contador
print(f"{contador} valores positivos")
print(round(media,1))