def minha_funcao(nome, **infos_adicionais):
    print ("Olá " + nome)

    if "nota_tp" not in infos_adicionais:
        print ("Nota TP não informada")
        return

    if infos_adicionais.get("nota_tp") > 7:
        print ("Aprovado")
    else:
        print ("Reprovado")

minha_funcao("Aluno", nota_tp = int(input("Digite a nota TP: ")))