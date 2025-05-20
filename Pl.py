def encontrar_combinacoes(comprimentos, limite):
    solucoes = set()

    def backtrack(combinacao, total):
        if total > limite:
            return

        pode_adicionar = False
        for comp in comprimentos:
            if total + comp <= limite:
                pode_adicionar = True
                break
                
        if not pode_adicionar and total > 0:
            desperdicio = limite - total
            if tuple(tuple(combinacao + [total] + [desperdicio])) not in solucoes:
                print(combinacao)
            solucoes.add(tuple(combinacao + [total] + [desperdicio]))
            return

        for i, comp in enumerate(comprimentos):
            nova_combinacao = combinacao[:]
            nova_combinacao[i] += 1
            backtrack(nova_combinacao, total + comp)

    combinacao_inicial = [0] * len(comprimentos)
    backtrack(combinacao_inicial, 0)

    return solucoes

def printar_solucoes(solucoes):
    for s in solucoes: 
        total = s[-2]
        desperdicio = s[-1]
        partes = []
        for qtd, tamanho in zip(s[:-1], comprimentos):
            partes.append(f"{qtd} barras de {tamanho} metros")
        frase = " + ".join(partes)
        print()
        print(f"{frase} | total = {total} metros | desperdicio = {desperdicio} metros")

def montar_desperdicio(solucoes):
    desperdicio = []
    for s in solucoes:
        desperdicio.append(s[-1])
    return desperdicio

def montar_matriz_respostas(solucoes):
    return [list(s[:-2]) for s in solucoes]

def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = [[0 for _ in range(linhas)] for _ in range(colunas)]
    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = matriz[i][j]
    return transposta


comprimentos = [50, 60, 80]
limite = 150

solucoes = encontrar_combinacoes(comprimentos, limite)

matriz_repostas = montar_matriz_respostas(solucoes)

print(matriz_repostas)


matriz_coeficientes = transpor_matriz(matriz_repostas)
print(matriz_coeficientes)

desperdicio = montar_desperdicio(solucoes)
n = len(desperdicio)
limitantes = [70,100,120]


