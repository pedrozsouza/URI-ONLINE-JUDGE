a,b,c = map(float,input().split())

areaTriangulo = (a * c)/2
areaCirculo = 3.14159 * (c * c)
areaTrapezio = ((a + b) * c) / 2
areaQuadrado = b * b
areaRetangulo = a * b

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")