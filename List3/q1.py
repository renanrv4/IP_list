n_animais = int(input())

animais = []
n = 0

# Loop para rodar enquanto o número de animais não foi listado
while n < n_animais:
    comando = input()
    
    # Condições para o comando de adicionar um animal
    if comando == 'REGISTRA':
        animal = input()
        if animal in animais:
            print(f'{animal} já foi registrado antes!')
        else:
            print(f'{animal} registrado com sucesso.')
            animais.append(animal)
            n += 1

    # Apaga o último animal inserido
    elif comando == 'CORRIGE':
        if len(animais) >= 1:
            del(animais[-1])
            print('Último registro apagado com sucesso.')
            n -= 1
        else:
            print('O catálogo ainda está vazio.')
            n = 0    
    # Apaga toda a lista independente da situação
    elif comando == 'REINICIA':
        animais = []
        print('Catálogo redefinido com sucesso.')
        n = 0

print('Todos os animais foram registrados!\n')
print('Catálogo de animais:')
# Imprime o catálogo de animais
for a in range(len(animais)):
    print(f'{a+1}º: {animais[a]}')