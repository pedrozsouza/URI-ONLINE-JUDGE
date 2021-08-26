x = int(input())
dentro = 0
fora = 0
for c in range(0,x):
    c = int(input())
    if 20>=c>=10:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} in")
print(f"{fora} out")
