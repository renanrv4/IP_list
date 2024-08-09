# "Quero deixar meu Pokemon mais forte!" → Adição
# "Deixa eu testar esse cogumelo estranho…" → Subtração
# "Vou evoluir meu Pokemon!" → Multiplicação
# "Não! Essa comida diminui o ataque…" → Divisão
# "E se eu colocar essa Mega Stone…" → Potenciação
# "Essa Mega Stone está estranha..." → Radiciação

# Operações a serem realizadas com o status do pokémon e o valor do item
# Adição, subtração, multiplicação, divisão, potenciação e radiciação
def adicao(status: int, valor: int):
    return status + valor

def subtracao(status: int, valor: int):
    return status - valor

def multiplicacao(status: int, valor: int):
    return status*valor

def divisao(status: int, valor: int):
    return status/valor

def potencia(status: int, valor: int):
    return status**valor

def radiciacao(status: int, valor: int):
    return status**(1/valor)

#------------------


# Quantidade de operações que o usuário vai realizar
qtd_acoes = int(input())

# O usuário resolveu não realizar nenhuma operação
if qtd_acoes == -1:
    print('Acho que vou desistir, confio no meu Pokemon sem nenhum item!')
else:
    for q in range(qtd_acoes):
        operacao = ''
        resultado = 0
        acao = input()
        status_pokemon = int(input())
        valor_item = int(input())

        # Realização das ações escolhidas de acordo com a entrada
        if acao == 'Quero deixar meu Pokemon mais forte!':
            operacao = 'Adição'
            resultado = adicao(status_pokemon, valor_item)

        elif acao == 'Deixa eu testar esse cogumelo estranho…':
            operacao = 'Subtração'
            resultado = subtracao(status_pokemon, valor_item)

        elif acao == 'Vou evoluir meu Pokemon!':
            operacao = 'Multiplicação'
            resultado = multiplicacao(status_pokemon, valor_item)

        elif acao == 'Não! Essa comida diminui o ataque…':
            operacao = 'Divisão'
            resultado = int(divisao(status_pokemon, valor_item))

        elif acao == 'E se eu colocar essa Mega Stone…':
            operacao = 'Potenciação'
            resultado = potencia(status_pokemon, valor_item)

        elif acao == 'Essa Mega Stone está estranha…':
            operacao = 'Radiciação'
            resultado = int(radiciacao(status_pokemon, valor_item))
        
        # Resultado final após cada ação
        print(f'Ao dar esse item eu esperava uma operação de {operacao} e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}')
    
    print('Agora tenho confiança que vou vencer!')
