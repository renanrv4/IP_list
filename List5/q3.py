# Função para observar se a palavra da senha está na charada do orc
def palavra_in_linha(words: list, linha, linha_completa=[]):
    indexsum = 0
    
    # Realizando a checagem de cada palavra
    for w in words:
        # Se a palavra estiver na linha, então ela é removida da lista de palavras
        if linha.startswith(w):
            words.remove(w)
            return palavra_in_linha(words, linha_completa, linha_completa)
        # Caso contrário ainda há a checagem dessa palavra
        else:
            if len(linha) > 0:
                return palavra_in_linha(words, linha[indexsum+1:], linha_completa)
    # Todas as palavras foram encontradas, a charada foi resolvida
    if len(words) == 0:
        return True

# Input da charada do orc
linha_orc = input()
n_frase = 0
decifrado = False

condicao = True
while condicao:
    frase = input()
    n_frase += 1
    # Frase que marca o FIM do jogo
    if frase == 'Decifra-me ou te devoro!':
        condicao = False
    else:
        frase_res = frase.split(' ')
        if palavra_in_linha(frase_res, linha_orc, linha_orc):
            print(f'Já sei, a senha é a frase número {n_frase}')
            decifrado = True

if not decifrado:
    print('Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas')
