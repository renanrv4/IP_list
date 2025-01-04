# Mensagem inicial
print("Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!")

# Enigma 1: Materiais mágicos
print("Quantos materiais mágicos estão trancados nos baús?")
qtd_materiais = int(input())
print("Vamos começar desbloqueando os materiais!")

materiais_desbloqueados = 0

for ordem_material in range(1, qtd_materiais + 1):
    print(f"Material {ordem_material} de {qtd_materiais}")
    nome_item = input("Senha mágica: ").strip().upper()

    # Exibir nome oculto
    estado_material = ""
    for char in nome_item:  # "char" vem de "character" = "caractere"
        estado_material += "_" if char != " " else " "
    print(estado_material)
    tamanho = len(nome_item)
    if tamanho <= 5:
        tentativas_restantes = 7
    elif tamanho <= 10:
        tentativas_restantes = 9
    elif tamanho <= 13:
        tentativas_restantes = 13
    else:
        tentativas_restantes = 16

    letras_chutadas = ""

    while tentativas_restantes > 0:
        letra = input().strip().upper()  # Variável para receber o chute da letra
        tentativas_restantes -= 1

        if tentativas_restantes == 0 and (letra not in nome_item or letra in letras_chutadas):
            print("Infelizmente não conseguimos descobrir a senha.")

        # Fui obrigada a criar uma condicional específica para um caso que estava dando um erro que não deveria no output gabarito.
        # Se quiser que eu explique, chama no discord.
        if letra in nome_item:
            ocorrencias = 0
            for char in nome_item:
                if char == letra:
                    ocorrencias += 1
            if letra not in letras_chutadas:
                if ocorrencias == 1:
                    print(f"Acertamos uma letra! Ela aparece um total de {ocorrencias} vez na senha")
                else:
                    print(f"Acertamos uma letra! Ela aparece um total de {ocorrencias} vezes na senha")

            if letra not in letras_chutadas:
                letras_chutadas += letra

            # Atualiza como está o estado do nome do material com as letras chutadas até o presente momento
            novo_estado = ""

            for char in nome_item:
                if char in letras_chutadas or char == " ":
                    novo_estado += char
                else:
                    novo_estado += "_"
            estado_material = novo_estado

            if "_" not in estado_material:  # Encerra o while, caso a senha for descoberta
                print(f"Parabéns! Você desbloqueou o material mágico '{nome_item}'!")
                materiais_desbloqueados += 1
                break

        elif tentativas_restantes > 0:
            print("Erramos a letra! Porém ainda temos mais tentativas.")

        if "_" in estado_material and tentativas_restantes == 0:  # Se for a última tentativa e a senha não for descoberta, ele imprime:
            print(f"Você não conseguiu desbloquear o material. O nome correto era '{nome_item}'.")

print(f"Você desbloqueou {materiais_desbloqueados} de {qtd_materiais} materiais mágicos!")

# Enigma 2: Código perdido
print("Os duendes precisam decifrar os códigos perdidos para montar o trenó!")
print("Quantas partes o trenó possui?")

qtd_partes = int(input())

partes_montadas = 0

for ordem_parte in range(1, qtd_partes + 1):

    print(f"Parte {ordem_parte} de {qtd_partes}")
    numeros = input().strip().split(' ')  # Variável para receber o chute da sequência de números

    menor = int(numeros[0])
    maior = int(numeros[0])

    # Descobrir o menor e maior número manualmente
    for num in numeros:
        num = int(num)
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    numero_magico = menor + maior

    print(f"Dica: O menor número é {menor} e o maior número é {maior}.")
    print(f"Descubra o número mágico (soma de {menor} e {maior})")

    tentativas_restantes = 2
    while tentativas_restantes > 0:
        tentativa = int(input())  # Variável para o chute do número mágico
        if tentativa == numero_magico:
            print(f"Você decifrou o código da parte {ordem_parte}! O trenó está mais próximo de ficar completo!")
            partes_montadas += 1
            break
        else:
            print("Número incorreto! Tente novamente.")
            tentativas_restantes -= 1
            if tentativas_restantes != 0:
                print(f"Descubra o número mágico (soma de {menor} e {maior})")
    if tentativas_restantes == 0:
        print(f"Você não conseguiu decifrar o código. O número mágico era {numero_magico}.")

print(f"Você montou {partes_montadas} de {qtd_partes} partes do trenó!")

# Mensagem final
if partes_montadas == qtd_partes:
    print("Parabéns! O trenó está completo e pronto para voar!")
elif partes_montadas >= qtd_partes // 2:
    print("Bom trabalho! O trenó quase ficou completo!")
else:
    print("Parece que o trenó ficou incompleto. Tente novamente na próxima missão!")
