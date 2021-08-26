n1,n2,n3,n4 =input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

nota1 = (n1 * 2)
nota2 = (n2 * 3)
nota3 = (n3 * 4)
nota4 = (n4 * 1)
media = (nota1 + nota2 + nota3 + nota4) / 10
print(f"Media: {round(media,1)}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    notaExame = float(input())
    print(f"Nota do exame: {round(notaExame,1)}")
    notaFinal = (media + notaExame) / 2
    if notaFinal >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {round(notaFinal,1)}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {round(notaFinal,1)}")
