# Listando os itens e trabalhos
itens = []
trabalhos = ['agricultura', 'criação', 'pesca', 'mineração']
for it in range(0, 4):
    item = input().split(' - ')
    itens.append(item)

print('Itens selecionados! Hora de iniciar a mesclagem... Simbora!')

combinando = True
while combinando:
    # Escolhendo os itens
    print('Combinando Itens...')
    inlist = []
    for i in range(0, 4):
        n = int(input())
        inlist.append(itens[i][n])
    # Imprimindo cada item escolhido com seu trabalho respectivo
    for li in range(len(inlist)):
        print(f'Item para {trabalhos[li]}: {inlist[li]}')

    opiniao = input()
    if opiniao == 'Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...':
        print('Meu dia tá garantido, obrigado pela ajuda Pega Móvel!')
        combinando = False
    elif opiniao == 'Esses itens são bem paia, acho que não gostei muito :(':
        comando = input()
        if comando == 'Bom, vamos tentar mais uma vez...':
            combinando = True
        elif comando == 'Essa máquina deve estar com defeito...':
            print('É... acho que já chega de Stardew por hoje...')
            combinando = False
        
