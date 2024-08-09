# Função para criar um cifra dos nomes de cada participante e cada pokémon
def cifra(nome, pokemon, passos, tempo):
    nome_result = ''
    pokemon_result = ''
    nomep = nome.lower()
    pokemon_nome = pokemon.lower()
    # Transformando os nomes utilizando a cifra de cesar
    for l in nomep:
        letter = (chars.index(l)+3)%26
        nome_result += chars[letter]
    
    for p in pokemon_nome:
        letter = (chars.index(p)+int(passos))%26
        pokemon_result += chars[letter]

    ascii_id(nome_result, pokemon_result, tempo, pokemon, nome)

# Função para transformar a cifra de cada nome em um código ASCII
def ascii_id(nome_cifra, pokemon_cifra, tempo_encontro, poke_name, nome_part):
    id_participante = 0
    id_pokemon = 0
    # Transformando as cifras em um número utilizando o valor ASCII de cada letra
    for l in nome_cifra:
        id_participante += ord(l)
    for p in pokemon_cifra:
        id_pokemon += ord(p)
    id_pokemon*=int(tempo_encontro)

    pokemon_shiny(id_participante, id_pokemon, nome_part, poke_name)

# Função para checar se o pokémon é shiny
def pokemon_shiny(id_participante, id_pokemon, np, nome_pokemon):
    nome_ind = participantes.index(np)
    id_nome = str(id_participante)
    id_poke =str(id_pokemon)
    # Checando se o pokémon é shiny
    if id_nome[-1] == id_poke[-1]:
        shiny = True
    else:
        shiny = False

    # Checagem caso o pokémon seja shiny e seja um pokémon favorito
    if shiny and pokemon_fav_list[nome_ind] == nome_pokemon and nome_pokemon not in participante_shinies[nome_ind]:
        if qtd_pokebolas_list[nome_ind] == 1:
            pokemon_fav_shiny.append(nome_pokemon)
            print(f'{np}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!')
        elif qtd_pokebolas_list[nome_ind] > 1:
            pokemon_fav_shiny.append(nome_pokemon)
            print(f'{np}: Consegui capturar um {pokemon_fav_list[nome_ind]} shiny!')
        elif qtd_pokebolas_list == 0:
            print(f'{np}: Só pode ser brincadeira, um {pokemon_fav_list[nome_ind]} shiny logo agora?!')
    # Checagem para caso o pokémon seja shiny, porém não é favorito
    elif shiny and pokemon_fav_list[nome_ind] != nome_pokemon and nome_pokemon not in participante_shinies[nome_ind]:
        if qtd_pokebolas_list[nome_ind] >= 1:
            print(f'{np}: Mais um shiny para a coleção, mas ainda não é um {pokemon_fav_list[nome_ind]}')
    # O pokémon é shiny e não é o favorito, porém as pokébolas acabaram
    elif shiny and pokemon_fav_list[nome_ind] != nome_pokemon and qtd_pokebolas_list[nome_ind] == 0:
        print(f'{np}: Péssimo momento, encontrei um {nome_pokemon} shiny, mas não tenho mais pokébolas!')

    # Checagem para caso o pokémon seja shiny e já tenha sido capturado
    elif shiny and nome_pokemon in participante_shinies[nome_ind]:
        print(f'{np}: Achei um {nome_pokemon} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...')
    # Checagem para caso o pokémon não seja shiny, porém é seu pokémon favorito
    elif not shiny and pokemon_fav_list[nome_ind] == nome_pokemon:
        if qtd_pokebolas_list[nome_ind] >= 1:
            print(f'{np}: Uau, um {pokemon_fav_list[nome_ind]}! Pena que não é um shiny...')
        elif qtd_pokebolas_list[nome_ind] == 0:
            print(f'{np}: Desculpa, meu querido {pokemon_fav_list[nome_ind]}, mas não poderei lhe capturar hoje')
    # Checagem para caso o pokémon nem seja favorito nem shiny
    elif not shiny and pokemon_fav_list[nome_ind] != nome_pokemon:
        if qtd_pokebolas_list[nome_ind] == 0:
            print(f'{np}: Só um {nome_pokemon} normal?Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...')
        elif qtd_pokebolas_list[nome_ind] >= 1:
            print(f'{np}: Ainda não é um {pokemon_fav_list[nome_ind]} shiny, tenho que continuar procurando...')

    # Caso o pokémon seja favorito, ou shiny o participante vai usar uma pokébola
    if nome_pokemon == pokemon_fav_list[nome_ind] or shiny:
        if qtd_pokebolas_list[nome_ind] >= 1 and nome_pokemon not in participante_shinies[nome_ind]:
            qtd_pokebolas_list[nome_ind] -= 1
        if shiny:
            participante_shinies[nome_ind].append(nome_pokemon)
    
chars = 'abcdefghijklmnopqrstuvwxyz'
n_participantes = int(input())

# Listas de participantes, pokémons favoritos, e quantidade de pokébolas de cada participante
participantes = []
pokemon_fav_list = []
qtd_pokebolas_list = []

# Lista das capturas shinies, e uma captura de um shiny favorito
participante_shinies = [[]]
pokemon_fav_shiny = []
for n in range(n_participantes):
    row = []
    participante_shinies.append(row)

for n in range(n_participantes):
    info_participantes = input().split(' ')
    # Olá, meu nome é Cesar, meu pokémon preferido é Zoroark e tenho 1 pokébolas
    #                 list[4]                        list[9]         list[-2]
    nome_participante = info_participantes[4][:-1]
    participantes.append(nome_participante)
    pokemon_fav = info_participantes[9]
    pokemon_fav_list.append(pokemon_fav)
    qtd_pokebolas = info_participantes[-2]
    qtd_pokebolas_list.append(int(qtd_pokebolas))

condicao = True
while condicao:
    info_encontro = input().split(' ')
    # Um Pikachu selvagem apareceu! Foram 51 segundos e 34 passos desde o último encontro de Thomaz
    #    list[1]                          list[5]       list[8]                              list[-1]
    pokemon = info_encontro[1]
    tempo = info_encontro[5]
    passos = info_encontro[8]
    participante = info_encontro[-1]
    cifra(participante, pokemon, passos, tempo)
    
    participante_index = participantes.index(participante)

    if len(pokemon_fav_shiny) >= 1:
        condicao = False

print('\n---Vamos verificar o que todos encontraram!---')
# Verificando as capturas shinies de cada participante
for p in participantes:
    nome_index = participantes.index(p)
    if len(participante_shinies[nome_index]) > 0:
        print('', end=f'{p} capturou os seguintes shinies: ')
        for pokemon_participante in range(len(participante_shinies[nome_index])):
            if participante_shinies[nome_index][pokemon_participante] != participante_shinies[nome_index][-1]:
                print('', end=f'{participante_shinies[nome_index][pokemon_participante]}, ')
            else:
                print(f'{participante_shinies[nome_index][pokemon_participante]}')
    else:
        print(f'Coitado, {p} não conseguiu capturar um único shiny hoje')
