voltas = int(input())
clima = input()
dificuldade = input()
pneu = input()

durabilidade = 0

# Durabilidade
if pneu == 'duro':
  durabilidade = 90
elif pneu == 'médio':
  durabilidade = 70
elif pneu == 'macio' or pneu == 'chuva':
  durabilidade = 50

# Pneus em condições desfavoráveis
if pneu == 'chuva' and clima == 'sol':
  durabilidade -= voltas*15
elif pneu != 'chuva' and clima == 'chuva':
  durabilidade -= voltas*15

# Clima ensolarado
if clima == 'sol' and dificuldade == 'baixa' or dificuldade == 'média' and pneu == 'macio' or pneu == 'médio':
  durabilidade -= voltas*2
elif clima == 'sol' and dificuldade == 'alta' and pneu == 'macio':
  durabilidade -= voltas*3
elif clima == 'sol' and dificuldade == 'alta' and pneu == 'duro':
  durabilidade -= voltas

# Clima com chuva
if clima == 'chuva' and dificuldade == 'baixa' and pneu == 'chuva':
  durabilidade -= voltas
elif clima == 'chuva' and dificuldade == 'média' and pneu == 'chuva':
  durabilidade -= voltas*2
elif clima == 'chuva' and dificuldade == 'alta' and pneu == 'chuva':
  durabilidade -= voltas*3

if durabilidade >= 20:
  print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.')
elif durabilidade < 20:
  print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')
  
  
  