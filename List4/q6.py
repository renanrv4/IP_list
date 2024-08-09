# Função para adiocionar pokémons 
def capturar_pokemons(qtd_poke, qtd_add, count):
    result_add = qtd_poke + qtd_add
    # Utilizando o contador para definir o valor que vai ser passado para a função de criar caixas
    if count == 0:
        create_box(result_add, 1, count)
    else:
        create_box(qtd_add, 1, count)
    return result_add

# Função para transferir pokémons
def transferir_pokemons(qtd_pokem, qtd_remove, count):
    result_transfer = qtd_pokem - qtd_remove
    # Utilizando o contador para definir o valor que vai ser passado para a função de criar caixas
    if count == 0:
        create_box(result_transfer, 0, count)
    else:
        create_box(qtd_remove, 0, count)
    return result_transfer

# Função para criar BOXES
def create_box(result, op, count_first):
    espaco = True
    result_comp = result
    # Enquanto espaço for true ele vai adicionar BOXES
    while espaco:
        box = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],]
        # Definindo a condição para adicionar boxes
        if result_comp > 0 and op == 1 or count_first == 0:
            if boxes[-1][-1][-1] == 1:
                boxes.append(box)
                result_comp -= 30
        # Guardando os pokémons na matriz
        if op == 1 or count_first == 0:
            for linhas in range(len(boxes[-1])):
                for colunas in range(len(boxes[-1][linhas])):
                    while result > 0 and boxes[-1][linhas][colunas] != 1:
                        boxes[-1][linhas][colunas] = 1
                        result -= 1
        # Retirando os pokémons da matriz 
        else:
            # Como a retirada de pokémons deve ser feita de forma contrária a captura
            # Então pode ser feita a inversão da matriz
            matriz_inversa = []
            boxes[-1] = inverter_matriz(boxes[-1], matriz_inversa)
            matriz_inversa = boxes[-1]
            for linhas in range(len(boxes[-1])):
                for colunas in range(len(boxes[-1][linhas])):
                    while result > 0 and boxes[-1][linhas][colunas] != 0:
                        boxes[-1][linhas][colunas] = 0
                        result -= 1
            matriz = []
            # Invertendo novamente para restaurar a matriz
            boxes[-1] = inverter_matriz(matriz_inversa, matriz)
        if len(boxes) > 2 and boxes[-1][0][0] == 0:
            del(boxes[-1])
        if result == 0 or boxes[1][0][0] == 0:
            espaco = False

# Função para inverter a matriz
def inverter_matriz(matriz, nova_matriz: list):
    for l in range(len(matriz)):
        nova_matriz.append(matriz[-(l+1)][::-1])
    return nova_matriz

# Quantidade de pokémons armazenados
qtd_pokemon_armazenados = int(input())

# Contador para definir a quantidade de pokémons que vai ser enviada para a função
count_n = 0

boxes = [[]]
box = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],]

condicao = True
while condicao:
    # Definindo quais ações vão ser feitas
    acao = input()
    if len(boxes) == 1:
        boxes.append(box)
    if acao != 'Finalizar':
        
        qtd_pokemon = int(input())
        # Ação de captura dos pokémons
        if acao == 'Capturar':
            qtd_pokemon_armazenados = capturar_pokemons(qtd_pokemon_armazenados, qtd_pokemon, count_n)
            count_n += 1
        # Ação de transferência dos pokémons
        elif acao == 'Transferir':
            qtd_pokemon_armazenados = transferir_pokemons(qtd_pokemon_armazenados, qtd_pokemon, count_n)
            if qtd_pokemon_armazenados < 0:
                qtd_pokemon_armazenados = 0
            count_n += 1
        
        # Impressão de todas as BOXES que estão sendo ocupadas por pokémons
        for box_number in range(1, len(boxes)):
            print(f'BOX {box_number}:')
            for linhas_box in range(len(boxes[box_number])):
                for colunas_box in range(len(boxes[box_number][linhas_box])):
                    if colunas_box+1 != len(boxes[box_number][linhas_box]):  
                        print('', end=f'{boxes[box_number][linhas_box][colunas_box]} ')
                    else:
                        print('', end=f'{boxes[box_number][linhas_box][colunas_box]}')
                print('')
            print('')

    elif acao == 'Finalizar':
        condicao = False

print('RELATÓRIO FINAL:\n')
print(f'BOXES: {len(boxes)-1}')
print(f'POKEMONS: {qtd_pokemon_armazenados}')