# Lista de Itens necessários
itens = input().split(', ')

# Lista de Itens presentes
lista_itens = input().split(', ')

itens_presentes = []

# Comparação da Lista de desejos com a lista de itens
for i in itens:
    for l in lista_itens:
        if i == l:
            itens_presentes.append(i)

# Catálogo dos Itens 
if len(itens_presentes) == 0:
    print(f'Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {len(itens)} itens aqui na fazenda.')
elif len(itens_presentes) >= 1:
    print('Estes são os itens que já tenho na fazenda:')
    for i in range(len(itens_presentes)):
        print(f'{i+1}º item: {itens_presentes[i]}')

    if len(itens_presentes) == len(itens):
        print(f'Perfeito, encontrei todos os {len(itens)} itens aqui na fazenda!')
    else:
        itens_faltantes = len(itens) - len(itens_presentes)
        print(f'Vou precisar adquirir {itens_faltantes} itens antes do festival!')

    print('Estou pronto para o festival de Stardew Valley! Que comece a diversão!')