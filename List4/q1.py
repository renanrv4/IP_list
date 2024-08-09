# CP Máximo = (Ataque * (Defesa**0.5) * (Stamina**0.5) * (CP Multiplicador**2)) / 10

# Ataque: é o valor do ataque base do Pokémon.

# Defesa: é o valor da defesa base do Pokémon.

# Stamina: é o valor da stamina base do Pokémon.

# CP Multiplicador: é um valor específico para cada nível do Pokémon.

# Função para calcular e armazenar os cps de pokémons diferentes
def calcular_cp (pokemons_list: list, cp_list: list):
    condicao = True
    while condicao:
        # Pokémon adicionado ou fim da adição
        pokemon = input()
        if pokemon == 'Fim':
            condicao = False
        if condicao:
            # Checagem da existência do pokémon na lista
            if pokemon not in pokemons_list:
                # Atributos e cálculo do CP 
                qt_ataque = int(input())
                qt_defesa = int(input())
                qt_stamina = int(input())
                multiplicador = float(input())
                cp = (qt_ataque * (qt_defesa**0.5) * (qt_stamina**0.5) * (multiplicador**2)) / 10
                cp_list.append(cp)
                pokemons_list.append(pokemon)
                print('Pokémon computado com sucesso.')
            else:
                print('Opa, esse Pokémon já foi analisado.')    
    
    pokemons_empate = []
    cps_empate = []
    # Análise dos cps de cada pokémon para indicar quem tem o maior CP
    for p in range(len(pokemons_list)):
        maior_cp = True
        empate = False
        for p1 in range(len(pokemons_list)):
            if pokemons_list[p] != pokemons_list[p1]:
                # O pokémon não tem o maior CP
                if cp_list[p] < cp_list[p1]:
                    maior_cp = False
                # Checagem caso aconteça um empate
                elif maior_cp and cp_list[p] == cp_list[p1]:
                    maior_cp = False
                    pokemons_empate.append(pokemons_list[p])
                    cps_empate.append(cp_list[p])
                    empate = True
        # Fim do programa, um pokémon com o maior CP já foi encontrado
        if maior_cp:
            print(f'O Pokémon com o maior CP na região de Kanto é: {pokemons_list[p]}, com CP máximo de {cp_list[p]:.2f}')
        elif empate and p == len(pokemons_list)-1:
            decidir_empate(pokemons_empate, cps_empate)

# Função para determinar o vencedor, quando há um empate entre dois ou mais pokémons com CPs empatados
def decidir_empate (nomes_pokemon: list, cps: list):
    for pok1 in nomes_pokemon:
        maior_char = True
        for pok2 in nomes_pokemon:
            if len(pok1) < len(pok2):
                maior_char = False
        if maior_char:
            cps_index = nomes_pokemon.index(pok1)
            print(f'Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {pok1}, com CP máximo de {cps[cps_index]:.2f}')
     
pokemons = []
cps = []
calcular_cp(pokemons, cps)
