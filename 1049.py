palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())
resultado = ''

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            resultado = 'aguia'
        elif palavra3 == "onivoro":
            resultado = "pomba"
    elif palavra2 == "mamifero":
        if palavra3 == "onivoro":
            resultado = 'homem'
        elif palavra3 == "herbivoro":
            resultado = "vaca"
elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            resultado = 'pulga'
        elif palavra3 == "herbivoro":
            resultado = "lagarta"
    elif palavra2 == "anelideo":
        if palavra3 == "hematofago":
            resultado = 'sanguessuga'
        elif palavra3 == "onivoro":
            resultado = "minhoca"
print(resultado)