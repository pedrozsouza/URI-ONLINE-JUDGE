a = float(input())

if a <= 400.00:
    novoSalario = (a * 0.15) + a
    reajuste = a * 0.15
    percentual = 15
elif 400.01 <= a <= 800.00:
    novoSalario = (a * 0.12) + a
    reajuste = a * 0.12
    percentual = 12
elif 800.01 <= a <= 1200.00:
    novoSalario = (a * 0.10) + a
    reajuste = a * 0.10
    percentual = 10
elif 1200.01 <= a <= 2000.00:
    novoSalario = (a * 0.07) + a
    reajuste = a * 0.07
    percentual = 7
elif a > 2000.00:
    novoSalario = (a * 0.04) + a
    reajuste = a * 0.04
    percentual = 4

print('Novo salario: {:.2f}'.format(novoSalario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))