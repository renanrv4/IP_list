# Função para realizar o cálculo de dano nas batalhas de pokémon 
def calc_dano(nv, nvpoder, defesa_inimigo, poder_atk, tipo, tipo_inimigo):
    # dano = ((((2* nível) + 10) / 250) * (poder/defesa_inimigo * poder_ataque) + 2) * (efetividade)
    dano = int(((((2* nv) + 10) / 250) * (nvpoder/defesa_inimigo * poder_atk) + 2) * (calc_efetividade(tipo, tipo_inimigo)))
    return dano

# Função para determinar a efetividade dos tipos de pokémon
def calc_efetividade(tipo, tipo_inimigo): 
    # Tabela Efetividade ---
    # tipo| fraco contra | forte contra | neutro contra
    # fogo | agua | grama| fogo e normal
    # agua | grama| fogo | agua e normal
    # grama | fogo | agua | grama e normal
    # normal| nenhum | nenhum | todos

    efetividade = 0

    if tipo == 'fogo':
        if tipo_inimigo == 'agua':
            efetividade = 0.5
        elif tipo_inimigo == 'grama':
            efetividade = 2
        elif tipo_inimigo == 'fogo' or tipo_inimigo == 'normal':
            efetividade = 1
    elif tipo == 'agua':
        if tipo_inimigo == 'grama':
            efetividade = 0.5
        elif tipo_inimigo == 'fogo':
            efetividade = 2
        elif tipo_inimigo == 'agua' or tipo_inimigo == 'normal':
            efetividade = 1
    elif tipo == 'grama':
        if tipo_inimigo == 'fogo':
            efetividade = 0.5
        elif tipo_inimigo == 'agua':
            efetividade = 2
        elif tipo_inimigo == 'grama' or tipo_inimigo == 'normal':
            efetividade = 1
    elif tipo == 'normal':
        efetividade = 1

    return efetividade

info_pokemon = input().split(', ')
# 'Charmander, fogo, 5, 39, 52, 43, 65, brasa, 40'
# nome (str), tipo (str), nível (int), vida(int), poder (int), defesa (int), velocidade (int), nome do ataque (str) e poder do ataque (int)
# Informações relacionadas ao pokémon
nome = info_pokemon[0]
tipo = info_pokemon[1]
# Nível e status
nivel =      int(info_pokemon[2])
vida =       int(info_pokemon[3])
poder =      int(info_pokemon[4])
defesa =     int(info_pokemon[5])
velocidade = int(info_pokemon[6])
vida_total = int(info_pokemon[3])
# Informações relacionadas ao ataque
nome_ataque = info_pokemon[7]
poder_atk = int(info_pokemon[8])

print(f'escolho você {nome}')

# Condição para caso haja um encontro entre a equipe rocket
# E se ela foi derrotada ou não
equipe_rocket = False
equipe_derrotada = False

# Condição para caso o seu pokémon tenha sido derrotado
pokemon_derrotado = False

# O pokémon inimigo ainda não foi definido
pokemon_inimigo_status = True

# As ações vão continuar até o momento em que a equipe rocket for derrotada, ou o seu pokémon foi derrotado
while not equipe_derrotada and not pokemon_derrotado:
    acontecimento = input()
    # Encontro com um pokémon selvagem
    if acontecimento == 'um pokemon selvagem aparece!':
        pokemon_batalha = []
        pokemon_batalha = input().split(', ')
        print('vamo botar pra quebrar!')
        print()
    # Encontro com a equipe rocket
    elif acontecimento == 'Equipe Rocket':
        pokemon_batalha = []
        pokemon_batalha = input().split(', ')
        equipe_rocket = True
        print(f'{nome}, bora acabar com a raça desses bandidos e salvar o professor!')
        print()
    
    # Definindo os status do pokémon inimigo
    if pokemon_inimigo_status:
        # Informações do pokémon da batalha
        nome_batalha = pokemon_batalha[0]
        tipo_batalha = pokemon_batalha[1]
        # Nível e status
        nivel_batalha =      int(pokemon_batalha[2])
        vida_batalha =       int(pokemon_batalha[3])
        poder_batalha =      int(pokemon_batalha[4])
        defesa_batalha =     int(pokemon_batalha[5])
        velocidade_batalha = int(pokemon_batalha[6])
        vida_total_inimigo = int(pokemon_batalha[3])
        # Informações relacionadas ao ataque
        nome_ataque_batalha = pokemon_batalha[7]
        poder_atk_batalha = int(pokemon_batalha[8])

        pokemon_inimigo_status = False

    # Ação de correr
    if acontecimento == 'correr' and equipe_rocket:
        print('lascou, eles não largam do meu pé!')
    elif acontecimento == 'correr' and not equipe_rocket:
        print('ufa, consegui meter o pé!')
        # Redefinindo o pokémon, após a fuga
        pokemon_inimigo_status = True

    # Ação de atacar
    if acontecimento == 'atacar':

        # A ordem dos turnos é definida de acordo com a velocidade dos pokémons
        if velocidade >= velocidade_batalha:
            vida_batalha -= calc_dano(nivel, poder, defesa_batalha, poder_atk, tipo, tipo_batalha)
            print(f'{nome} usou {nome_ataque}')
            efetividade = calc_efetividade(tipo, tipo_batalha)
            if efetividade == 2: 
                print('foi super efetivo!')
            elif efetividade == 0.5:
                print('não foi muito efetivo')

            if vida_batalha > 0:
                vida -= calc_dano(nivel_batalha, poder_batalha, defesa, poder_atk_batalha, tipo_batalha, tipo)
                print(f'{nome_batalha} usou {nome_ataque_batalha}')
                efetividade_inimigo = calc_efetividade(tipo_batalha, tipo)
                if efetividade_inimigo == 2: 
                    print('foi super efetivo!')
                elif efetividade_inimigo == 0.5:
                    print('não foi muito efetivo')
        else:
            vida -= calc_dano(nivel_batalha, poder_batalha, defesa, poder_atk_batalha, tipo_batalha, tipo)
            print(f'{nome_batalha} usou {nome_ataque_batalha}')
            efetividade_inimigo = calc_efetividade(tipo_batalha, tipo)
            if efetividade_inimigo == 2: 
                print('foi super efetivo!')
            elif efetividade_inimigo == 0.5:
                print('não foi muito efetivo')
            
            if vida > 0:
                vida_batalha -= calc_dano(nivel, poder, defesa_batalha, poder_atk, tipo, tipo_batalha)
                print(f'{nome} usou {nome_ataque}')
                efetividade = calc_efetividade(tipo, tipo_batalha)
                if efetividade == 2: 
                    print('foi super efetivo!')
                elif efetividade == 0.5:
                    print('não foi muito efetivo')

        # A vida dos pokémons não pode ser negativa
        if vida < 0:
            vida = 0
        elif vida_batalha < 0:
            vida_batalha = 0

        # Print dos HPs após o turno
        print(f'HP: {vida}/{vida_total} | HP inimigo: {vida_batalha}/{vida_total_inimigo}')

        # Checagem para caso os pokémons tenham sido derrotados
        if vida == 0:
            print(f'{nome} derrotado!')
            # Seu pokémon foi derrotado
            pokemon_derrotado = True
            print()
            print('Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
        elif vida_batalha == 0:
            # O pokémon inimigo foi derrotado
            print(f'{nome_batalha} derrotado!')
            pokemon_inimigo_status = True
            print()
            if equipe_rocket:
                print(f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome}?')
                equipe_derrotada = True



