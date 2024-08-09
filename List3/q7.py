matriz = []
dimensoes = input().split(' x ')
# Dimensões X e Y da matriz
linhas = int(dimensoes[0])
colunas = int(dimensoes[1])

# Preenchendo a matriz com zeros
for li in range(linhas):
    row = []
    for co in range(colunas):
        row.append(0)
    matriz.append(row)

qtd_elementos = int(input())

for e in range(qtd_elementos):
    elemento = input().split(' ')
    nv_atrativo = int(elemento[0])
    # Coordenadas da matriz Y - X
    # Utilizando string slicing e split para armazenar as coordenadas
    coords = elemento[1].split(',')
    y = int(coords[0][1:])
    x = int(coords[1][:-1])
    for lin in range(linhas):
        for col in range(colunas):
            matriz[y][x] = nv_atrativo

condicao = True
while condicao:
    acao = input()
    # Permutando os elementos escolhidos na matriz
    if acao == 'Permutar':
        coordenadas = input().split(')')
        # (i,j) (k,l)
        # Utilizando string slicing e split para armazenar as coordenadas
        coords1 = coordenadas[0].split(',')
        coords2 = coordenadas[1].split(',')
        i = int(coords1[0][1:])
        j = int(coords1[1])
        k = int(coords2[0][2:])
        l = int(coords2[1])
        # Permutando as valores
        matriz[i][j], matriz[k][l] = matriz[k][l], matriz[i][j]
    # Realizando uma transposição da matriz com uma nova matriz
    elif acao == 'Transposição':
        nova_matriz = []
        for col in range(colunas):
            row = []
            for lin in range(linhas):
                row.append(0)
            nova_matriz.append(row)

        for l in range(linhas):
            for c in range(colunas):
                if matriz[l][c] != 0:
                    nova_matriz[c][l] = matriz[l][c]

        linhas, colunas = colunas, linhas
        matriz = nova_matriz
    elif acao == 'Remover':
        # Fazendo uma comparação entre todos os elementos da matriz X e Y
        qtd_remove = 0
        for y1 in range(linhas):
            for x1 in range(colunas):
                menor = 0
                for y2 in range(linhas):
                    for x2 in range(colunas):
                        if matriz[y1][x1] != 0 and matriz[y2][x2] != 0:
                            if matriz[y1][x1] <= matriz[y2][x2]:
                                continue
                            else:
                                menor = 1
                if menor == 0 and qtd_remove == 0 and matriz[y1][x1] != 0:
                    # Coordenadas do elemento a ser removido
                    matriz[y1][x1] = 0
                    qtd_remove += 1

    elif acao == 'Fim':
        condicao = False

print('Atual Arranjo:')
for l in range(linhas):
    for c in range(colunas):
        if c+1 != colunas:
            print(f'{matriz[l][c]}', end=' ')
        else:
            print(f'{matriz[l][c]}', end='')
    print('')




