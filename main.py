def listar_readme():
    arquivo_readme = open("readme.md", "r", encoding="utf-8")
    print("readme: ")
    print(arquivo_readme.read())


def escrever_readme():
    texto = input("O que deseja adicionar ao readme? ")
    arquivo_readme = open("readme.md", "a", encoding="utf-8")
    arquivo_readme.write("\n\n" + texto)
    arquivo_readme.close()

listar_readme()
escrever_readme()
listar_readme()