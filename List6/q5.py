def generos_mais_escutados(generos_escutados, musicas_lista, generos_list):
    generos_result = {}
    # Converte o dicionário das músicas de cada gênero em duas listas
    # Para que seja possível realizar a ordenação baseado nos valores de cada item do dicionário 
    qtd_list = list(generos_escutados.values())
    qtd_list.sort(reverse=True)
    generos_nome = list(generos_escutados.keys())
    for qtd in qtd_list:
        if qtd != 0:
            # Adicionando ao dicionário apenas os gêneros com pelo menos uma música que foi escutada
            for gen_nome in generos_nome:
                if generos_escutados[gen_nome] == qtd:
                    generos_result[gen_nome] = qtd
    # Identificando quais são os valores do top3 
    top3, val_top = [], []
    lista_comparacao = list(generos_result.values())
    lista_temp = list(generos_result.values())
    for _ in range(3):
        top3.append([])
        condicao, condicao_troca = True, True
        lista_comparacao = lista_temp
        for val in range(len(lista_comparacao)):
            if condicao:
                valor = lista_comparacao[0]
                condicao = False
            # Se o valor for igual ao valor da lista de comparação
            # O valor é adicionado ao top3
            if valor == lista_comparacao[val] and valor not in val_top:
                top3[_].append(valor)
            # Se o valor não for igual alteramos a lista de comparação
            elif condicao_troca:
                lista_temp = lista_comparacao[val:]
                condicao_troca = False
        val_top.append(valor)
    # Função para determinar todas as recomendações
    return recomendacoes(top3, musicas_lista, generos_list, generos_result)

def recomendacoes(top_gen, musicas, generos_musicas_list, list_gen):
    recomendacoes_dict = {}
    musicas_recommend = []
    top1, top2, top3 = [], [], []
    top_index = 0

    # Identificando quais são os gêneros que estão no top3, de acordo com seu valor de músicas escutadas
    for top in top_gen:
        for gen in list_gen.keys():
            if len(top) > 0:
                if list_gen[gen] == top[0] and top_index == 0:
                    top1.append(gen)
                elif list_gen[gen] == top[0] and top_index == 1:
                    top2.append(gen)
                elif top_index == 2 and gen not in top1 and gen not in top2:
                    top3.append(gen)
        top_index += 1

    # Músicas recomendadas para o (s) gênero(s) no top1, top2, top3
    top_rank, _top_ind = (top1, top2, top3), 3
    for _top in top_rank:
        for _top_rank in _top:
            recomendacoes_dict[_top_rank] = []
            music_add = 0
            list_musicas = generos_musicas_list[_top_rank]
            for _music in list_musicas:
                if _music not in musicas and music_add < _top_ind:
                    recomendacoes_dict[_top_rank].append(_music)
                    musicas_recommend.append(_music)
                    music_add += 1
        _top_ind -= 1
    # Retornando o dicionário e a lista com as músicas recomendadas    
    return (recomendacoes_dict, musicas_recommend)

# Dicionário de todos os gêneros e músicas
generos_musicais = {
    'Samba': ('Preciso Me Encontrar', 'O Mundo É Um Moinho', 'Trem Das Onze', 'O Que É O Que É?', 'Disritmia', 'Timoneiro'),
    'Rock Nacional': ('Epitáfio', 'Meu Novo Mundo', 'À Sua Maneira', 'Que País É Este', 'Um Minuto Para O Fim Do Mundo', 'Infinita Highway'),
    'Rock': ('Smells Like Teen Spirit', 'In The End', 'Californication', 'Welcome To The Jungle', 'Another Brick In The Wall', 'Bohemian Rapsody', 'Bring Me To Life', 'Paint It, Black', 'Stairway To Heaven'),
    'Pop': ('As It Was', 'Viva La Vida', 'Someone Like You', 'Blinding Lights', 'Maps', 'Talking To The Moon', 'Believer', 'Ghost', 'Wake Me Up', 'Rude', 'Perfect'),
    'MPB': ('O Descobridor Dos Sete Mares', 'Anunciação', 'Exagerado', 'João E Maria', 'Sujeito De Sorte', 'Naquela Mesa', 'Eduardo E Mônica', 'Lanterna Dos Afogados', 'Metamorfose Ambulante'),
    'Manguebeat': ('Da Lama Ao Caos', 'A Praieira', 'Maracatu Atômico', 'Manguetown', 'Um Sonho', 'A Cidade'),
    'Indie Folk': ('Ends Of The Earth', 'Welcome Home, Son', 'Riptide', 'Father And Son', 'Ho Hey', 'The Night We Met', 'Budapest', 'Atlantis'),
    'Forró': ('Xote Das Meninas', 'Xote Da Alegria', 'Deus Me Proteja', 'Numa Sala De Reboco', 'Meu Cenário', 'Colo De Menina', 'Riacho Do Navio')
}

# Inputs
nome_usuario = input()
qtd_musicas = int(input())

# Gerando um dicionário para descobrir quais gêneros foram escutados
generos_list = list(generos_musicais.keys())
generos_escutados = dict.fromkeys(generos_list, 0)
musicas_escutadas = []

if qtd_musicas > 0:
    for qtd in range(qtd_musicas):
        musica = input()
        musicas_escutadas.append(musica)
        # Adicionando ao dicionário de gêneros escutados
        for gen in generos_musicais.keys():
            if musica in generos_musicais[gen]:
                generos_escutados[gen] += 1

    # Chamando a função para definir quais foram os gêneros mais escutados,
    # e o dicionário de recomendações
    resultado = generos_mais_escutados(generos_escutados, musicas_escutadas, generos_musicais)
    if len(resultado[1]) > 0:
        print(f'{nome_usuario} escutou {qtd_musicas} música(s) e estas são as próximas recomendações:\n')
        qtd_m = 0
        for _res in resultado[0].values():
            for _music_res in _res:
                qtd_m += 1
                print(f'{qtd_m}. {_music_res}')
    else:
        print('', end=f'{nome_usuario} já escutou todas as músicas disponíveis no(s) gênero(s): ')
        generos_result = []
        for _genero_name in generos_musicais.keys():
            for _gen_result in resultado[0].keys():
                if _gen_result == _genero_name:
                    generos_result.append(_gen_result) 
        if len(generos_result) == 1:
            print(f'{generos_result[0]}. Infelizmente não sobrou nenhuma música disponível para recomendação.')
        else:
            for _genero in generos_result:
                if _genero != generos_result[-1]:
                    if _genero == generos_result[-2]:
                        print('', end=f'{_genero} ')
                    else:
                        print('', end=f'{_genero}, ')
                else:
                    print(f'e {_genero}. Infelizmente não sobrou nenhuma música disponível para recomendação.')
else:
    print(f'Parece que {nome_usuario} não escutou nenhuma música. Vamos recomendar algumas músicas de gêneros diferentes:\n')
    for i  in range(len(list(generos_musicais.keys()))):
        print(f'{i+1}. {generos_musicais[generos_list[i]][0]}')
