# Torre do Mago - 700m - 6:00 às 23:00
# Rancho da Marnie - 260m - 9:00 às 16:00
# Saloon - 1,2km - 12:00 às 00:00
# Armazém do Pierre - 1,1km - 09:00 às 17:00
# Casa do Prefeito - 1,5km - 08:30 às 22:00
# Peixaria - 1,9km - 09:00 às 17:00
# Museu - 1,87km - 08:00 às 18:00
# Ferreiro - 1,7km - 09:00 às 16:00
# Mercado Joja - 1,8km - 09:00 às 23:00
# Carpintaria - 1,5km - 09:00 às 17:00
# Minas - 1,85km - Todo o dia
# Centro Comunitário - 1,3km - Todo o dia

locais = ['Torre do Mago', 'Rancho da Marnie', 'Saloon', 'Armazém do Pierre', 'Casa do Prefeito', 'Peixaria', 'Museu', 'Ferreiro', 'Mercado Joja', 'Carpintaria', 'Minas', 'Centro Comunitário']
distancias = [700, 260, 1200, 1100, 1500, 1900, 1870, 1700, 1800, 1500, 1850, 1300]
horarios = [['06', '00', '23', '00'], ['09', '00', '16', '00'], ['12', '00', '24', '00'], ['09', '00', '17', '00'], ['08', '30', '22', '00'], ['09', '00', '17', '00'], ['08', '00', '18', '00'], ['09', '00', '16', '00'], ['09', '00', '23', '00'], ['09', '00', '17', '00'], ['00', '00', '24', '00'], ['00', '00', '24', '00']]
suspeitos = ['Artur', 'João', 'Luana',' Pedro Elias','Thomaz', 'Welton']

# Culpados por causa de um local não existente - Local
nome_culpado = []
nome_locais = []

# Culpados por mentir sobre o horário - Horário
nome_culpado_h = []
nome_locais_h = []
horario_fechamento = []
culpados_encontrados = False

# Suspeitos próximos da plantação - Distância
nome_culpado_d = []
nome_locais_d = []
distancia = []

for s in suspeitos:
    # nome - horário (hh:mm) - local  
    alibi = input().split(' - ')
    horario = alibi[1].split(':')
    hh = int(horario[0])
    mm = int(horario[1])

    # Encontrando os culpados
    # Condição para indicar se os culpados já foram encontrados
    lugar = False

    # Culpado(s) que mentiram sobre o local
    if alibi[2] not in locais:
        nome_locais.append(alibi[2])
        nome_culpado.append(alibi[0])
        lugar = True

    # Condição para indicar se os culpados já foram encontrados
    horario = False
    
    # Culpado(s) que mentiram sobre o horário
    if lugar == False:
        local_ind = locais.index(alibi[2])
        if int(horarios[local_ind][0]) <= hh <= int(horarios[local_ind][2]):
            if hh == int(horarios[local_ind][0]) or hh == int(horarios[local_ind][2]):
                if int(horarios[local_ind][1]) <= mm <= int(horarios[local_ind][3]):
                    culpados_encontrados = False
            else:
                culpados_encontrados = False
        else:
            if alibi[2] not in nome_locais_h:
                nome_locais_h.append(alibi[2])
            nome_culpado_h.append(alibi[0])
            if int(horarios[local_ind][2]) == 24:
                horario_fechamento.append('00')
                horario_fechamento.append('00')
            else:
                horario_fechamento.append(horarios[local_ind][2])
                horario_fechamento.append(horarios[local_ind][3])
            horario = True
    
    # Suspeito(s) que estavam próximos da plantação
    if lugar == False and horario == False:
        local_index = locais.index(alibi[2])
        nome_culpado_d.append(alibi[0])
        distancia.append(distancias[local_index])

# Culpado(s) pelo roubo de melões pela informação falsa sobre o local
# Uma pessoa mentiu sobre o local
if len(nome_culpado) == 1:
    print(f'Esse lugar {nome_locais[0]} nem existe! {nome_culpado[0]} foi quem roubou os melões!')
    culpados_encontrados = True
# Mais de uma pessoa mentiu sobre o local
elif len(nome_culpado) > 1:
    nome_locais.sort()
    for l in nome_locais:
        if l != nome_locais[-1]:
            print('', end=f'{l}, ')
        else:
            print('', end=f'{l} ')
    print('', end='nem existem! ')
    nome_culpado.sort()
    for c in nome_culpado:
        if c != nome_culpado[-1]:
                print('', end=f'{c}, ')
        else:
            print('', end=f'{c} ')
    print('roubaram os melões!')
    culpados_encontrados = True

# Culpado(s) pelo roubo de melões pela informação falsa sobre o horário
if culpados_encontrados == False:

    # Apenas uma pessoa mentiu sobre o horário
    if len(nome_culpado_h) == 1:
        print(f'{nome_locais_h[0]} nem estava aberto nessa hora, esse lugar foi fechado às {horario_fechamento[0]}:{horario_fechamento[1]}! {nome_culpado_h[0]} roubou os melões!')
        culpados_encontrados = True

    # Mais de uma pessoa mentiu sobre o horário
    elif len(nome_culpado_h) > 1:
        nome_locais_h.sort()
        for l in nome_locais_h:
            if l != nome_locais_h[-1]:
                print('', end=f'{l}, ')
            else:
                print('', end=f'{l} ')
        print('', end='nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! ')
        nome_culpado_h.sort()
        for c in nome_culpado_h:
            if c != nome_culpado_h[-1]:
                print('', end=f'{c}, ')
            else:
                print('', end=f'{c} ')
        print('se uniram e roubaram os melões!')
        culpados_encontrados = True

# Suspeitos por estarem próximos a plantação
if culpados_encontrados == False:
    distancia_menor = []
    # Encontrando as menores distâncias
    for d in distancia:
        menor = True
        for dcomparacao in distancia:
            if d > dcomparacao:
                menor = False
        if menor:
            distancia_menor.append(d)
    
    # Apenas uma pessoa estava próxima do rouba
    if len(distancia_menor) == 1:
        nome_index = distancia.index(distancia_menor[0])
        print(f'{nome_culpado_d[nome_index]} estava a {distancia_menor[0]} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!')
    # Mais de uma pessoa estava próxima
    elif len(distancia_menor) > 1:
        culpados = []
        for nc in nome_culpado_d:
            nome_index = nome_culpado_d.index(nc)
            if distancia[nome_index] == distancia_menor[0]:
                culpados.append(nc)
        culpados.sort()
        for c in culpados:
            if c != culpados[-1]:
                print('', end=f'{c}, ')
            else:
                print('', end=f'{c} ')
        print(f'estavam a {distancia_menor[0]} metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!')