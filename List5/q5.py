# Função para gerar as combinações possíveis
def gerar_combinacoes(valores, indice=0, combinacao=[]):

    if indice == len(valores):
        # Se atingiu o fim da lista de valores, retorna a combinação atual
        return [combinacao]

    # Lista de Valores e variável que indica se existe uma possibilidade
    combinacoes = []
    existe_opcao = False

    # Loop que observa os valores na lista para criar as combinações
    for valor in valores[indice]:
        # Se o valor não estiver na combinção ele é adicionado
        if valor not in combinacao:
            novas_combinacoes = gerar_combinacoes(valores, indice + 1, combinacao + [valor])
            combinacoes.extend(novas_combinacoes)
            existe_opcao = True

    # Se não existe nenhuma outra opção então é adicionado a string 'nada'
    if not existe_opcao:
        novas_combinacoes = gerar_combinacoes(valores, indice + 1, combinacao + ['nada'])
        combinacoes.extend(novas_combinacoes)
    
    return combinacoes

# Função para processar todas as possibilidades de batalha com o Boss
def n_possibilidades(n_jogadores, vida_max, vida, list_primos, list_armas, tipos_jogador=[], tipos_utilizados=[], todos_tipos=[], possibilidades=[], index=0, ciclo=0, copia_tipos=[]):
    vida_perdida = 0
    cycle_index = ciclo%n_jogadores

    # Adicionando a lista dos tipos de arma que cada jogador vai usar na rodada
    if (cycle_index)%n_jogadores == 0:
        for player in range(n_jogadores):
            tipos_jogador.append([]) 

    # Lista para os tipos utilizados pelo jogador na batalha
    if ciclo == 0:
        for players in range(n_jogadores):
                tipos_utilizados.append([])

                
    if vida > 0:
        # Possíveis armas que podem ser usadas contra o boss
        for arma in range(len(list_armas[cycle_index])):
            if vida%list_primos[arma] == 0:
                tipos_jogador[cycle_index].append(list_primos[arma])
                todos_tipos.append(list_primos[arma])
        
        if (cycle_index+1)%n_jogadores == 0:
            # Gerando as possibilidades de acordo com as armas
            possibilidades = gerar_combinacoes(tipos_jogador)
            has_number = False

            # Loop de todas os casos possíveis
            for casos in possibilidades:
                
                # Utilizando list comprehension para criar uma cópia de cada elemento dentro de tipos utilizados
                # Assim a lista cópia tipos sempre é atualizada quando ocorre uma volta da recursão
                copia_tipos = [el.copy() for el in tipos_utilizados]

                # Se a sequência for maior que 0, então quer dizer que existe um resultado em que o boss foi derrotado
                if len(sequencia_atual) == 0:
                    vida += vida_perdida
                    
                    vida_perdida = 0

                    # Checando cada caso
                    for caso in range(len(casos)):
                        if type(casos[caso]) == int:
                            has_number = True
                        if casos[caso] != 'nada':
                            caso_index = list_primos.index(casos[caso])
                            primo_index = casos.index(casos[caso])
                            if vida_perdida < vida:
                                copia_tipos[primo_index] += [casos[caso]]
                            else:
                                copia_tipos[primo_index] += ['nada']
                            vida_perdida += int(list_armas[primo_index][caso_index])
                        else:
                            copia_tipos[caso].append('nada')
                    
                    if not has_number:
                        return False
                    else:
                        vida -= vida_perdida
                        # Se a vida do boss for menor ou igual a 0, então o Boss foi derrotado
                        if vida <= 0:
                            sequencia_atual.append(copia_tipos)
                            return True
                        # Caso contrário as outras possibilidades vão ser observadas
                        else:
                            x = n_possibilidades(n_jogadores, vida_max, vida, list_primos, list_armas, [], copia_tipos.copy(), [], [], index, ciclo+1)
                else:
                    return True
                        
        # Trocando o jogador, para realizar a checagem das armas
        else:
            x = n_possibilidades(n_jogadores, vida_max, vida, list_primos, list_armas, tipos_jogador, tipos_utilizados, todos_tipos, possibilidades, index, ciclo+1)
    else:
        return True

# Variáveis inicias
n_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
n_jogadores = int(input())
nicks, armas_jogador, sequencia_atual = [], [], []

for n in range(n_jogadores):
    # Jogadores e suas armas
    jogador = input().split(' ')
    nick = jogador[0]
    qtd_armas = jogador[1]
    nicks.append(nick)

    # Dano de cada arma
    dano_armas = input().split(' ')
    armas_jogador.append(dano_armas)

# Vida do boss
vida_boss = int(input())

# Chamando a função para observar as possibilidades
n_possibilidades(n_jogadores, vida_boss, vida_boss, n_primos, armas_jogador)

# Se a sequência for maior que 0, então o boss foi derrotado
if len(sequencia_atual) > 0:
    print('Felizmente conseguimos vencer!')
    print('A seguinte sequencia de acoes pode ser usada:')
    # Impressão dos nicks de cada jogador e da sua sequência de ações
    for name in nicks:
        name_ind = nicks.index(name)
        print('', end=f'{name} ')
        for arma_usada in range(len(sequencia_atual[0][name_ind])):
            # Impressão de armas
            if sequencia_atual[0][name_ind][arma_usada] != 'nada':
                primo_indice = n_primos.index(sequencia_atual[0][name_ind][arma_usada])
                if (arma_usada+1) != len(sequencia_atual[0][name_ind]):
                    print('', end=f'arma_{primo_indice+1} ')
                else:
                    print('', end=f'arma_{primo_indice+1}')
            # O jogador não fez nenhuma ação na rodada
            else:
                if (arma_usada+1) != len(sequencia_atual[0][name_ind]):
                    print('', end=f'nada ')
                else:
                    print('', end=f'nada')
        print('')
# O boss não foi derrotado
else:
    print('Infelizmente nao conseguiremos vencer dessa vez.')