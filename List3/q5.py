# Lista de todos os peixes do vale
peixes = ['Anchova', 'Atum', 'Bagre', 'Baiacu', 'Cioba', 'Enguia', 'Esturjão', 'Linguado', 'Pepino-do-mar', 'Polvo', 'Salmão', 'Sardinha', 'Tilápia', 'Truta', 'Robalo']

# Conquistas de Pesca
conquistas = ['Pescador', 'Velho Marinheiro', 'Velho Pescador', 'Deus Pescador']

pescadores = 0
# Loop para verificar as conquistas de todos os pescadores
while pescadores < 3:
    # Condição para saber se estão peixe_pndo a verdade ou a mentira
    condicao = True

    # Separando o nome e conquista dos pescadores
    nome_conquista = input().split(': ')
    nome = nome_conquista[0]
    conquista = []
    if len(nome_conquista) > 1:
        if ',' in nome_conquista[1]:
            conquista = nome_conquista[1].split(', ')
        else:
            conquista.append(nome_conquista[1])
    
    # Peixes que cada pescador pescou
    peixes_pescados = []
    peixes_diferentes = []
    escrevendo_peixes = True
    while escrevendo_peixes:
        peixe_p = input()
        if peixe_p == 'FIM':
            escrevendo_peixes = False
        # Peixes com nomes diferentes
        elif peixe_p not in peixes_diferentes and peixe_p in peixes:
            peixes_diferentes.append(peixe_p)
        # Todos os peixes pescados
        if escrevendo_peixes and peixe_p in peixes:
            peixes_pescados.append(peixe_p)
    # Verificação da história de cada pescador
    if len(conquista) > 0:
        for conq in conquista:
            # Verificação de cada conquista
            if conq == 'Pescador':
                if 5 > len(peixes_diferentes):
                    condicao = False
            if conq == 'Velho Marinheiro':
                if 10 > len(peixes_diferentes):
                    condicao = False
            if conq == 'Velho Pescador':
                if 15 > len(peixes_diferentes):
                    condicao = False
            if conq == 'Deus Pescador':
                if len(peixes_pescados) < 25:
                    condicao = False
        if condicao:
            print(f'{nome} realmente estava falando a verdade!!!')
        else:
            print(f'{nome} é um mentiroso, ele não tem todas essas conquistas!')
    else:
        if len(peixes_diferentes) > 0:
            print(f'{nome} é um mentiroso, ele não tem todas essas conquistas!')
        else:
            print(f'{nome} realmente estava falando a verdade!!!')
    
    pescadores+=1