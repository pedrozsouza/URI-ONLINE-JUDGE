Nome = str(input())
salarioFixo = float(input())
Vendas = float(input())

salarioFinal = salarioFixo + (Vendas * 0.15)

print("TOTAL = R$ %0.2f" % salarioFinal)