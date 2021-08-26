a1 = int(input())
a2 = int(input())
a3 = int(input())

maquina = 0

resultado1 = (a2 * 2) + (a3 * 4)
resultado2 = (a1 * 2) + (a3 * 2)
resultado3 = (a1 * 4) + (a2 * 2)

menor = resultado1

if resultado2 < resultado1:
    menor = resultado2
if resultado2 > resultado3:
    menor = resultado3

print(menor)

