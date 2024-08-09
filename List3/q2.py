suspeitos = []

repeticao = True

while repeticao:
    decisao = input()
    # Adiocionar Suspeitos
    if decisao == 'Novo suspeito - altíssima periculosidade':
        nome = input()
        suspeitos.insert(0, nome)
    
    elif decisao == 'Novo suspeito - pouco perigoso':
        nome = input()
        suspeitos.append(nome)

    # Remover inocente
    elif decisao == 'Livre de suspeita, pode remover':
        nome = input()
        suspeitos.remove(nome)

    # Troca de Posições entre Suspeitos
    elif decisao == 'Sujeito mais perigoso do que pensávamos':
        posicao_suspeito = int(input())
        posicao_troca = int(input())
        suspeitos[posicao_suspeito], suspeitos[posicao_troca] = suspeitos[posicao_troca], suspeitos[posicao_suspeito]
    elif decisao == 'Que estranho, esses dois meliantes… troque-os de lugar':
        nome_suspeito = input()
        nome_troca = input()
        # Loop por toda a lista para trocar os nomes dos suspeitos
        for m in range(len(suspeitos)):
            if suspeitos[m] == nome_suspeito:
                suspeitos[m] = nome_troca
            elif suspeitos[m] == nome_troca:
                suspeitos[m] = nome_suspeito
        
    elif decisao == 'Essa posição não esta de acordo, ele não e tão perigoso assim':
        nome = input()
        # Removendo da Posição atual e movendo para o fim da lista
        suspeitos.remove(nome)
        suspeitos.append(nome)

    # Imprimindo a Lista de Suspeitos
    elif decisao == 'Como a lista esta ficando?':
        for s in suspeitos:
            if s != suspeitos[-1]:
                print(s, end=', ')
            else:
                print(s)
    elif decisao == 'Já temos nossa lista de suspeitos':
        print('O resultado final ficou assim:')
        for f in suspeitos:
            if f != suspeitos[-1]:
                print(f, end=', ')
            else:
                print(f)
        repeticao = False