x = int(input())
quadrado = 0
for c in range(1,x+1):
    if c%2==0:
        quadrado = c*c
        print(f"{c}^2 = {quadrado}")