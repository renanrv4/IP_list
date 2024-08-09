# Função para calcular o MDC
def MDC(x, y, n):
    # Se algum dos valores for 0, a função retorna o outro valor
    if x == 0:
        return y
    elif y == 0:
        return x
    
    # Se um número n é capaz de dividir ambos os números então o MDC é o valor de n
    if x%n == 0 and y%n == 0:
        return n
    # Caso contrário é utilizado uma função recursiva para subtrair um ao valor de n para realizar o processo novamente
    else:
        return MDC(x, y, n-1)

# Input da quantidade de pares a serem recebidos
qtd_pares = int(input())

# Variável para armazenar os resultados da  função de MDC
senha = 0

for q in range(qtd_pares):
    n_pares = input()
    pares = n_pares.split(' ')
    n1 = int(pares[0])
    n2 = int(pares[1])
    if n1 > n2:
        nmenor = n2
    else:
        nmenor = n1
    resultadoMDC = MDC(n1, n2, nmenor)    
    senha += resultadoMDC
    print(f'O MDC entre {n1} e {n2} é {resultadoMDC}')

print(f'\nA senha final foi {senha}')