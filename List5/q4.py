# Função para calcular a quantidade de megas
def megabytes(arquivos):
    # Total de megabytes
    total = 0
    # Lista para registrar os megabytes de cada item
    megas = []
    # Lista para armazenar o formato de todos os itens, por exemplo: [1, [3, 4]]
    pastas = []

    for arc in arquivos:
        # Caso o tipo do item seja uma lista, uma recursão é feita para analisar os itens dentro dessa lista
        if isinstance(arc, list):
            # Utilizando recursão para realizar a soma dos valores que estão dentro de uma lista
            # Ou seja, quando o elemento é uma lista a função para calcular os megas é chamada passando como parâmetro a pasta(lista) 
            total += megabytes(arc)

        # Caso contrário o valor em megas do item(arquivo) é somado ao total de megas
        else:
            total += arc
    # Adicionando o total de megas e formatos dos arquivos 
    megas.append(total)
    pastas.append(arquivos)

    # Imprimindo os valores em megabytes dos arquivos e o formato de todos os arquivos 
    # Primeiramente, apenas valores que já estão presentes em uma pasta devem ser printados, apenas no final valores que estão na raiz vão ser printados com todo o resto
    for result in range(len(pastas)):
        print(f'{megas[result]} -> {pastas[result]}')
    
    return total

# Input do arquivo
lista = eval(input())

# Chamando a função megabytes para receber o formato do arquivo e calcular os valores em mega de cada item no arquivo
megabytes(lista)
