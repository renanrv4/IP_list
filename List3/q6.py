professores = ['Anjolina', 'Ricardo', 'Stefan']
especies = []
n_especies = ['coelhos', 'galinhas', 'patos']
# Coelhos, Galinhas, Patos
li_animais = [0, 0, 0]

# Lista de itens
li_itens = []

# Itens - Para-raio
ferro = 0
quartzo = 0
asa = 0
para_raios = 0

for p in professores:
    # Parte de Anjolina
    if p == 'Anjolina':
        galinheiros = int(input())
        # Listando os animais
        for g in range(galinheiros):
            animais = input().split(', ')
            for a in animais:
                especies.append(a)
                
        for e in range(len(especies)):
            if especies[e] == 'Coelho':
                li_animais[0]+= 1
            elif especies[e] == 'Galinha':
                li_animais[1]+= 1
            elif especies[e] == 'Pato':
                li_animais[2]+= 1

        for ne in range(len(n_especies)):
            if li_animais[ne] >= 1:
                print(f'A fazenda tem {li_animais[ne]} {n_especies[ne]}!')
            else:
                print(f'Poxa que pena, não temos {n_especies[ne]}.')

    # Parte de Ricardo
    elif p == 'Ricardo':
        li_compras = input().split(', ')
        if 'Melão' in li_compras:
            print('Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...')
        li_vende = input().split(', ')

        # Comparando os itens de cada lista
        for item in li_compras:
            for item_vende in li_vende:
                if item == item_vende and item not in li_itens:
                    li_itens.append(item)

        # Final das compras
        if li_itens == li_compras:
            print('Consegui comprar todas as frutas que queria!')
        elif len(li_itens) == 0:
            print('Poxa, acho que ficaremos sem plantações.')
        else:
            print('Consegui comprar as seguintes sementes:')
            # Ordenando a lista por ordem alfabética
            li_itens.sort()
            for i in range(len(li_itens)):
                if li_itens[i] != li_itens[-1]:
                    print(f'{li_itens[i]}', end=', ')
                else:
                    print(f'{li_itens[i]}')

    # Parte de Stefan
    elif p == 'Stefan':
        materiais = input().split(', ')
        qtd_materiais = input().split(', ') 

        # Adição de Materiais
        for m in range(len(materiais)):
            if materiais[m] == 'Barra de ferro':
                ferro += int(qtd_materiais[m])
            elif materiais[m] == 'Quartzo refinado':
                quartzo += int(qtd_materiais[m])
            elif materiais[m] == 'Asa de morcego':
                asa += int(qtd_materiais[m])
        # Quantidade de Para-raios
        while ferro >= 1 and quartzo >= 1 and asa >= 5:
            para_raios += 1
            ferro -= 1
            asa -= 5
            quartzo -= 1
        print(f'Com os itens que tenho, consigo fazer {para_raios} para-raios!')
