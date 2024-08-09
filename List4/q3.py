# 0 → Vaporeon (Água);
# 1 → Jolteon (Elétrico);
# 2 → Flareon (Fogo);
# 3 → Espeon (Psíquico);
# 4 → Umbreon (Sombrio);
# 5 → Glaceon (Gelo);
# 6 → Leafeon (Planta);
# 7 → Sylveon (Fada).

# Água: Misty, Gary, Ivy, Blanche
# Elétrico: Ash, Ritchie, Surge, Spark
# Fogo: May, Blaine, Candela
# Psíquico: Agatha, Sabrina, Fantina
# Sombrio: Jessie, James, Giovanni
# Gelo: Lorelei, Dawn
# Planta: Max, Erika, Tracey, Mallow
# Fada: Whitney

# Função para identificar o treinador e sua evolução do eevee
def treinador(chrs, chrs_cap, trainers, nomecapitalized, idadetreinador):

    # Evoluções possíveis
    evolucoes = [f'A evolução do Eevee de {nomecapitalized} é para Vaporeon, o mestre das águas!', f'O Eevee de {nomecapitalized} evoluiu para Jolteon, cheio de energia elétrica!', 
                 f'O Eevee de {nomecapitalized} se transformou em Flareon, dominando o calor do fogo!', f'Espeon é a evolução do Eevee de {nomecapitalized}, mostrando sua mente brilhante!', 
                 f'A evolução sombria do Eevee de {nomecapitalized} é Umbreon, deslizando pelas sombras!', f'Glaceon é o novo estágio do Eevee de {nomecapitalized}, tão frio quanto o gelo!', 
                 f'O Eevee de {nomecapitalized} se transformou em Leafeon, um espírito da floresta!', f'Sylveon é a evolução mágica do Eevee de {nomecapitalized}, irradiando bondade e misticismo!']

    # Checagem para descobrir caso o treinador seja famoso
    checagem_realizada = False
    for t in range(len(trainers)):
        treinador_desconhecido = True
        for te in trainers[t]:
            # O treinador é famoso
            if nomecapitalized == te:
                treinador_desconhecido = False
                checagem_realizada = True
        if not treinador_desconhecido:
            print(evolucoes[t])
    # Caso o treinador não seja famoso, então o cálculo é realizado
    if treinador_desconhecido and checagem_realizada == False:
        # Chamando a função para realizar o cálculo
        print(evolucoes[calc_evolucao(nomecapitalized, idadetreinador, chrs, chrs_cap)])

# Função para definir a evolução eevee com base no cálculo:
# Somatório dos valores de cada letra, esse somatório multiplicado pela idade do treinador. E o resultado final é o resto de divisão por 8
def calc_evolucao(nome, idadetreinador, chars, chars_cap):
    somatorio = 0
    resultado = 0
    for l in nome:
        if l == nome[0]:
            first = chars_cap.index(l)
            somatorio += first+1
        else:
            indexl = chars.index(l)
            somatorio += indexl+1
    resultado = somatorio*idadetreinador
    return resultado%8

# Lista com todos os caracteres para comparação
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caracteres_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Lista de treinadores já conhecidos
treinadores_famosos = [['Misty', 'Gary', 'Ivy', 'Blanche'], # Vaporeon
                       ['Ash', 'Ritchie', 'Surge', 'Spark'], # Jolteon
                       ['May', 'Blaine', 'Candela'], # Flareon
                       ['Agatha', 'Sabrina', 'Fantina'], # Espeon
                       ['Jessie', 'James', 'Giovanni'], # Umbreon
                       ['Lorelei', 'Dawn'], # Glaceon
                       ['Max', 'Erika', 'Tracey', 'Mallow'], # Leafeon 
                       ['Whitney'] # Sylveon
                       ] 

qtd_treinadores = int(input())
for q in range(qtd_treinadores):
    # Nome e idade do treinador
    nome_idade = input()
    nome_idade = nome_idade.split(' - ')
    nome = nome_idade[0]
    idade = int(nome_idade[1])
    nomecap = nome.capitalize()
    # Chamando a função de treinador
    treinador(caracteres, caracteres_cap, treinadores_famosos, nomecap, idade)
