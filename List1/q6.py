cons1 = input()
posicao1 = int(input())
salario1 = int(input())

cons2 = input()
posicao2 = int(input())
salario2 = int(input())

pontos1 = 0
pontos2 = 0
  
# Pontos da contrutora
if cons1 == 'Red Bull':
  pontos1 = pontos1 + 3
elif cons1 == 'McLaren':
  pontos1 = pontos1 + 2
elif cons1 == 'Mercedes' or cons1 == 'Aston Martin':
  pontos1 = pontos1 + 1
  
if cons2 == 'Red Bull':
  pontos2 = pontos2 + 3
elif cons2 == 'McLaren':
  pontos2 = pontos2 + 2
elif cons2 == 'Mercedes' or cons2 == 'Aston Martin':
  pontos2 = pontos2 + 1
  
# Pontos de posição
if posicao1 == 1:
  pontos1 += 3 + (salario1 // 4)
elif posicao1 == 2:
  pontos1 += 2 + (salario1 // 4)
elif posicao1 == 3 and cons1 != 'Red Bull':
  pontos1 = 0

  
if posicao2 == 1:
  pontos2 += 3 + (salario2 // 4)
elif posicao2 == 2:
  pontos2 += 2 + (salario2 // 4)
elif posicao2 == 3 and cons2 != 'Red Bull':
  pontos2 = 0

if cons1 == 'Ferrari':
  pontos1 = 0
if cons2 == 'Ferrari':
  pontos2 = 0
  
#Decisão
if pontos1 == 0 and pontos2 == 0:
  print('Depois de tantas temporadas, o Sainz vai descançar em 2025.')
elif pontos1 > pontos2:
  print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {cons1}, que pontuou {pontos1}.')
elif pontos2 > pontos1:
  print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {cons2}, que pontuou {pontos2}.')
else: 
  print('As duas são ótimas opções! Vamos, Sainz!!')
   
  
  


