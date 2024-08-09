def calcular_lucro (discos):
    if 2 <= discos <= 3:
        return (discos * 20)*0.98
    elif 4 <= discos <= 5:
        return (discos * 20)*0.95
    elif discos >= 6:
        return (discos * 20)*0.93
    else:
        return (discos * 20)
    
artistas_list = [{'Priscila Senna': 10000.00, 'Eduarda': 9990.00, 'Academia da Berlinda': 9995.00, 'Martins': 9970.00, 'Igor de Carvalho': 9965.00}, {}]

lucro_1semana, semana_2 = {}, {}

n_artistas = int(input())
for n in range(n_artistas):
    artistas = input().split(' - ')
    nome, qtd_discos = artistas[0], int(artistas[1])
    lucro = calcular_lucro(qtd_discos)
    if nome not in artistas_list[0].keys():
        artistas_list[1][nome] = lucro
        semana_2[nome] = qtd_discos
    else:
        lucro_1semana[nome] = (lucro/artistas_list[0][nome])*100
        artistas_list[0][nome] += lucro

if len(lucro_1semana) > 0:
    print('Estes artistas obtiveram aumento do lucro em relação à primeira semana:')
    for artista in lucro_1semana:
        print(f'{artista} - Lucro em relação à primeira semana: {lucro_1semana[artista]:.2f}%')
else:
    print('Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!')

print('')

print('Esta é a fortuna atual dos artistas considerados:')
for art_li in artistas_list:
    for nome in art_li:
        print(f'{nome}: R$ {art_li[nome]:.2f}')

print('')

if len(semana_2) > 0:
    print('Na semana 2 tivemos vendas de novos artistas no mercado:')
    for art in semana_2:
        print(f'{art} - Discos vendidos: {semana_2[art]}')
else:
    print('Na semana 2 não tivemos vendas de novos artistas no mercado!')
