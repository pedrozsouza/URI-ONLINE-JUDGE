frango,bife,massa = map(int,input().split())
refeicoesF,refeicoesB,refeicoesM = map(int,input().split())

caso1=0

if refeicoesF > frango:
    caso1 = caso1 + (refeicoesF - frango)
if refeicoesB > bife:
    caso1 = caso1 + (refeicoesB - bife)
if refeicoesM > massa:
    caso1 = caso1 + (refeicoesM - massa)
print(caso1)