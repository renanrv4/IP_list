def calcular_pontos(top_position, ano_cidade, views_artista):
    if top_position == 0:
        return ano_cidade+(views_artista[top_position]*1000000)
    elif top_position == 1:
        return (ano_cidade//2)+(views_artista[top_position]*1000000)
    elif top_position == 2:
        return (ano_cidade//3)+(views_artista[top_position]*1000000)

def vencedor(artistas_famosos = {}):
    vencedor_index = list(artistas_famosos.values())
    maior_pontuacao = sorted(vencedor_index, reverse=True)
    artista_nome = list(artistas_famosos.keys())
    artista_vencedor = artista_nome[vencedor_index.index(maior_pontuacao[0])]
    if artista_vencedor == 'João Gomes':
        return ('Parabéns, João Gomes, o novo fenômeno da música pernambucana!', artista_vencedor)
    elif artista_vencedor == 'Zé Vaqueiro':
        return ('Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!', artista_vencedor)
    elif artista_vencedor == 'Raphaela Santos':
        return ('Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!', artista_vencedor)
    elif artista_vencedor == 'Alceu Valença':
        return ('Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!', artista_vencedor)
    elif artista_vencedor == 'Priscila Senna':
        return ('Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!', artista_vencedor)

artistas = {'João Gomes': 0, 'Zé Vaqueiro': 0, 'Raphaela Santos': 0, 'Alceu Valença': 0, 'Priscila Senna': 0}
musicas_top = {}
cidades = {}

n_vezes = int(input())

for n in range(n_vezes):
    cidade = input()
    cidades[n] = cidade
    ano_fundacao = int(input())
    views = {}
    musicas = {}
    for _ in range(3):
        artista_info = input().split(' - ')
        views[int(artista_info[2])] = artista_info[0]
        musicas[int(artista_info[2])] = artista_info[1]
    top3 = sorted(views, reverse=True)
    if n == 0 or views[top3[0]] not in musicas_top.keys() or musicas_top[views[top3[0]]][1] < top3[0]:
        musicas_top[views[top3[0]]] = (musicas[top3[0]], top3[0])
    for top_views in top3:
        artistas[views[top_views]] += calcular_pontos(top3.index(top_views), ano_fundacao, top3)

if 'Recife' in cidades.values():
    print('A veneza brasileira foi consultada nesta pesquisa!')
if 'Olinda' in cidades.values():
    print('Uma honra ver que a primeira capital pernambucana foi consultada!')
if 'Petrolina' in cidades.values():
    print('Ansioso para descobrir a opinião dos petrolinenses!')

resultado = vencedor(artistas)

print(resultado[0])
print(f'O fenômeno é {resultado[1]}, que canta a música {musicas_top[resultado[1]][0]}, já contando com mais de {musicas_top[resultado[1]][1]} milhões de visualizações na internet.')
