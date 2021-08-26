x = int(input())

anoFinal = x // 365
mesFinal = (x % 365 ) // 30
diaFinal = (x % 365)%30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anoFinal,mesFinal,diaFinal))







