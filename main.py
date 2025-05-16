def calcular_media(*notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media


print (calcular_media(5, 7, 8, 9))