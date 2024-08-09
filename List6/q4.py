# Função para calcular a diferença na quantidade de discos e ajustar os valores dos discos de cada artista
def calc_diferenca(qtd_discos, artistas_dict, art1, art2):
    _art1, _art2 = '', ''
    diferenca = qtd_discos[0] - qtd_discos[1]
    if diferenca != 0 and diferenca%3 == 0:
        if qtd_discos[0] > qtd_discos[1]:
            _art1, _art2 = art1, art2
        else: 
            _art1, _art2 = art2, art1
        for artista in artistas_dict.keys():
            for disco in artistas_dict[artista].keys():
                if artista == _art1:
                    artistas_dict[artista][disco][0] += 4.00
                else:
                    artistas_dict[artista][disco][0] -= 4.00
                    if artistas_dict[artista][disco][0] < 1.00 : artistas_dict[artista][disco][0] = 1.00
            
    return (diferenca, _art1, _art2)

# Inputs / Variáveis iniciais
artistas, musicas = {}, {}

discos_vendidos, total_discos, total_discos_temp = {}, [0, 0], [0, 0]
valor_arrecadado = [0, 0]

receita_total = 0.00
discos_vendidos_total = 0

ultima_diferenca = 0

artista_1 = input()
artista_2 = input()

for artista in [artista_1, artista_2]:
    condicao = True
    musicas = {}
    # Adicionando os discos de cada artista
    while condicao:
        comando = input()
        if comando != 'acabou':
            preco_disco = float(input())
            # Preço do disco e quantidade vendida
            musicas[comando] = [preco_disco, 0]
        else:
            condicao = False
    artistas[artista] = musicas

print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")
print(f'E os artistas de hoje são {artista_1} e {artista_2}!')
print('-----COMEÇO DO EXPEDIENTE!-----')

vendas = True
while vendas:
    disco_vendido = input()
    if disco_vendido != 'FIM':
        for _artista in list(artistas.keys()):
            # Adicionando o valor arrecadado com a venda e aumentado a quantidade de discos vendidos
            if disco_vendido in artistas[_artista].keys():
                artistas[_artista][disco_vendido][1] += 1
                if _artista == artista_1:
                    total_discos[0] += 1
                    total_discos_temp[0] += 1
                    valor_arrecadado[0] += artistas[_artista][disco_vendido][0]
                else:
                    total_discos[1] += 1
                    total_discos_temp[1] += 1
                    valor_arrecadado[1] += artistas[_artista][disco_vendido][0]
        print(f'{disco_vendido} vendido')
        # Cada vez que um disco é vendido, a função para calcular a diferença na quantidade de discos é chamada
        diff_res = calc_diferenca(total_discos_temp, artistas, artista_1, artista_2)
        if diff_res[0] != 0 and diff_res[0]%3 == 0:
            total_discos_temp = [0, 0]
            print(f'A diferença está ficando muito grande! AUMENTA R$4 DE {diff_res[1].upper()} E ABAIXA R$4 DE {diff_res[2].upper()}!')
    else:
        vendas = False
        print('-----FIM DO EXPEDIENTE!-----')

# Decidindo o ganhador
if valor_arrecadado[0] > valor_arrecadado[1]:
    ganhador = (artista_1, valor_arrecadado[0], total_discos[0])
else:
    ganhador = (artista_2, valor_arrecadado[1], total_discos[1])

if valor_arrecadado[0] == 0 and valor_arrecadado[1] == 0:
    receita_total = 0
else:
    receita_total = valor_arrecadado[0] + valor_arrecadado[1]
    discos_vendidos_total = total_discos[0] + total_discos[1]

print(f'O total de receita gerado foi de {receita_total} e foram vendidos {discos_vendidos_total} discos.')

if total_discos[0] == 0 and total_discos[1] == 0:
    print('Que tristeza! Só artista péssimo...')
elif valor_arrecadado[0] == valor_arrecadado[1]:
    print('Difícil de escolher o melhor!')
else:
    print(f'O artista que mais gerou dinheiro para a loja foi {ganhador[0]}, acumulando uma receita de {ganhador[1]} e vendendo {ganhador[2]} discos.')