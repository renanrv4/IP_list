espaco = 0
energia = 100

# Tipo de picareta
picareta = input()

# Tamanho da mochila
mochila = input()
if mochila == 'basica':
    espaco = 10
elif mochila == 'media':
    espaco = 20
elif mochila == 'grande':
    espaco = 30

# Espaço da picareta
espaco -= 1

# * - espaço vazio
# p - pedra
# a - carvão
# c - cobre
# f - ferro
# o - ouro
# b - barril
# e - escada
p = 0
a = 0
c = 0
f = 0
o = 0
b = 0
rubi = 0

# Itens já no inventário
p_inv = 0
a_inv = 0
c_inv = 0
f_inv = 0
o_inv = 0
rubi_inv = 0

# Itens do barril
itens_barril = []
barris_quebrados = []

# String - X(qtd) - Y(energia)
comida = input()
qtd = comida.split(' - ')
qtd_alimento = int(qtd[1])
energia_alimento = int(qtd[2])

# Quantidade de comida
if qtd_alimento == 1:
    print(f'Hoje, irei levar apenas uma unidade de {qtd[0]}.')
    espaco -= 1
elif qtd_alimento > 1:
    print(f'Bom estoque! vou levar {qtd_alimento} unidades de {qtd[0]}.')
    espaco -= 1 
else:
    print(f'Vai ser tenso, vou levar nada pra repor minha energia...')

# Número de andares da mina
andares = int(input())

fim = False
n = 0
# Loop que continua rodando enquanto a energia, ou espaço, ou o número de andares não acabarem
while n < andares and fim == False:
    energiagasta = 0
    matriz = []
    size = input().split()
    if int(size[0]) == int(size[1]):
        print(f'Poxa! Esse andar é um quadrado perfeito de lado {size[0]}!!!')
    else:
        print(f'Esse andar da caverna parece um retângulo ou uma matriz {size[0]}x{size[1]}. Depois de minerar, ela ficou assim:')
    row = []

    # Criação da matriz do tamanho do andar
    for y in range(int(size[0])):
        objetos = input().split()

        matriz.append(objetos)

    # Quebra de Minérios e Barris
    # Interando por todos os elementos da matriz
    for item in range(int(size[0])):
        for it in range(int(size[1])):
            itens_diff = []
            # Quebra de Barris
            if matriz[item][it] == 'b':
                matriz[item][it] = '*'
                itens_b = input().split(', ')
                b += 1
                energiagasta += 3
                rubi_encontrado = False
                # Caso tenha um rubi ele ignora todo o resto do barril
                if 'rubi' in itens_b:
                    rubi += 1
                    if rubi_inv == 0:
                        espaco -= 1
                        rubi_inv += 1
                    rubi_encontrado = True
                    barris_quebrados.append('rubi')
                # Caso contrário ele recebe os itens
                elif rubi_encontrado == False:
                    # Adicionando os itens encontrados e descobrindo os itens que já foram adicionados antes
                    for i in itens_b:
                        if i not in itens_barril:
                            itens_diff.append(i)
                        itens_barril.append(i)
                    espaco -= len(itens_diff)
                    barris_quebrados.append(itens_b)
                itens_diff = []
            # Quebra com Picareta Básica
            if picareta == 'basica' and matriz[item][it] != 'e' and matriz[item][it] != 'f' and matriz[item][it] != 'o' and matriz[item][it] != '*':
                if matriz[item][it] == 'p':
                    p+=1
                    if p_inv == 0:
                        p_inv +=1
                        espaco -= 1
                elif matriz[item][it] == 'a':
                    a+=1
                    if a_inv == 0:
                        a_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'c':
                    c+=1
                    if c_inv == 0:
                        c_inv += 1
                        espaco -= 1
                matriz[item][it] = '*'
                energiagasta += 3
            # Quebra com Picareta de Cobre
            elif picareta == 'cobre' and matriz[item][it] != 'e' and matriz[item][it] != 'o' and matriz[item][it] != '*':
                if matriz[item][it] == 'p':
                    p+=1
                    if p_inv == 0:
                        p_inv +=1
                        espaco -= 1
                elif matriz[item][it] == 'a':
                    a+=1
                    if a_inv == 0:
                        a_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'c':
                    c+=1
                    if c_inv == 0:
                        c_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'f':
                    f+=1
                    if f_inv == 0:
                        f_inv += 1
                        espaco -= 1
                matriz[item][it] = '*'
                energiagasta += 3

            # Quebra Picareta de Ferro
            elif picareta == 'ferro' and matriz[item][it] != 'e' and matriz[item][it] != '*':
                if matriz[item][it] == 'p':
                    p+=1
                    if p_inv == 0:
                        p_inv +=1
                        espaco -= 1
                elif matriz[item][it] == 'a':
                    a+=1
                    if a_inv == 0:
                        a_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'c':
                    c+=1
                    if c_inv == 0:
                        c_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'f':
                    f+=1
                    if f_inv == 0:
                        f_inv += 1
                        espaco -= 1
                elif matriz[item][it] == 'o':
                    o+=1
                    if o_inv == 0:
                        o_inv += 1
                        espaco -= 1
                matriz[item][it] = '*'
                energiagasta += 3

    # Matriz do andar após a mineração
    for linhas in range(int(size[0])):
        for colunas in range(int(size[1])):
            if colunas+1 != int(size[1]):
                print(f'{matriz[linhas][colunas]}', end=' ')
            else:
                print(f'{matriz[linhas][colunas]}', end='')
        print('')
    
    # Itens encontrados nos barris
    for barril in range(b):
        if barris_quebrados[barril] == 'rubi':
            print('MEU DEUS EU ACHEI UM RUBI NESSE BARRIL!!!')
        elif b >= 1:
            print(f'Opa, quebrei o {barril+1}º barril e recebi {len(barris_quebrados[barril])} itens.')
    b = 0 
    barris_quebrados = []

    # Energia Restante após o fim do andar
    energia -= energiagasta
    energiagasta = 0

    # Fim caso a energia tenha acabado
    if energia < 10 and qtd_alimento == 0 and n+1 != andares:
        print(f'To sem energia para continuar minerando. Pelo menos cheguei ao andar {n+1}.')
        fim = True
    elif qtd_alimento >= 1 and energia < 10:
        # Consumo da quantidade de alimentos(x) recuperando a energia(y)
        energia += (energia_alimento*qtd_alimento)
        x = 0
        if energia < 10 and n+1 != andares:
            print(f'To sem energia para continuar minerando. Pelo menos cheguei ao andar {n+1}.')
            fim = True

    # Fim dos andares
    if (n+1) == andares:
        print('Cheguei aonde eu queria por hoje, vou sair.')
        fim = True

    if fim == False and energia >= 10:
        print('Ainda dá pra continuar minerando, vamos simbora!!!')
    
    # Mais um andar
    n += 1 

# Prints após a saída da mina
print('Pronto, acabei de sair da mina. Vamos ver o que eu consegui:')

# Minérios obtidos
print(f'Total de pedra: {p}.')
print(f'Total de carvão: {a}.')
print(f'Total de cobre: {c}.')
print(f'Total de ferro: {f}.')
print(f'Total de ouro: {o}.')

if espaco <= 0:
    print('A bolsa volta cheia hoje :)')

if rubi >= 1:
    print('A mineração hoje foi incrível!!!')
else:
    print('A mineração foi boa, mas ainda estão falando que roubei os melões :(')