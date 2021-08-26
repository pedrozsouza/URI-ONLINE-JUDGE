tamanho = int(input())
numero = [int(c) for c in input().split()]
total = 1
for c in range(2, tamanho):
    if numero[c] - numero[c-1] != numero[c-1] - numero[c-2]:
        total += 1
print(total)