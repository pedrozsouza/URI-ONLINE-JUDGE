hs,tv,fh = input().split()
hs = int(hs)
tv = int(tv)
fh = int(fh)
resposta = hs + tv + fh

if 0 <= resposta < 24:
    print(resposta)
elif resposta >= 24:
    print(resposta - 24)
elif resposta< 0:
    print(resposta + 24)