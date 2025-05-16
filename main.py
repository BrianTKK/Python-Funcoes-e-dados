import sys

try:
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
except FileNotFoundError:
    print("Crie o arquivo readme.md para usar o programa.")
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    sys.exit(1)