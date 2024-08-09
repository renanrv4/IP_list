# Função para calcular os números para o login
def fatorial_login(n):
    if n != 0:    
        # Utilizando recursão para retornar as condições específicas do formato do login
        if n%2 == 0:
            return n*2 + fatorial_login(n-1)
        else:
            return n*3 + fatorial_login(n-1)
    else:
        return n

# Função para definir o login
def login(cod: list):
    result = ''
    # Utilizando a função de fatorial de login para definir o login
    for num in cod:
        result += str(fatorial_login(int(num)))
    return result

# Função para calcular o fatorial de um número qualquer
def fatorial_senha(n):
    if n == 0:
        return 1
    elif n > 1:
        # Utilizando recursão para retornar a função de fatorial e armazenar um novo valor
        return n * fatorial_senha(n-1)
    else:
        return n

# Função para definir a senha
def senha(cod: list):
    result = ''
    # Utilizando Fatorial para criar a senha
    for num in cod:
        result += str(fatorial_senha(int(num)))
    return result

# Exemplo de input: 2:4:1:3
num_sequence = input()
codigo = num_sequence.split(':')

# Output
print('As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!')
print(f'Login: {login(codigo)}')
print(f'Senha: {senha(codigo)}')
