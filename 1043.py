a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < b + c and ( a - c ) < b < a + c and ( a - b ) < c < a + b:
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)
