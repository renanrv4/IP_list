n_decisoes = int(input())

media = 0
pontos = 0

for x in range(n_decisoes):
  praticas = input()
  if praticas == 'Programar utilizando uma boa IDE':
    pontos += 5
  elif praticas == 'Programar sem utilizar IDE':
    pontos -= 5
  elif praticas == 'Códigos limpos e organizados':
    pontos += 10
  elif praticas == 'Código bagunçado e mal estruturado':
    pontos -= 6
  elif praticas == 'Nomenclatura objetiva e de fácil identificação de variáveis':
    pontos += 7
  elif praticas == 'Nomenclatura confusa e difícil de identificar variáveis':
    pontos -= 5
  elif praticas == 'Assistir às aulas do REDU':
    pontos += 10
  elif praticas == 'Comentários significativos':
    pontos += 5
  elif praticas == 'Evitar repetições desnecessárias de códigos':
    pontos += 5
  elif praticas == 'Tirar dúvidas com os monitores e professores':
    pontos += 10
  else:
    pontos -=10
    
if pontos < 0:
  pontos = 0
elif n_decisoes == 0:
  media = 0
else:
  media = pontos / n_decisoes

if media > 10:
  media = 10

if media < 3:
  print('É melhor voltar a cantar mesmo!')
elif 3 < media < 7:
  print('Vai precisar se esforçar um pouco mais, meu cantor!')
elif media == 7:
  print('Na conta certa!')
elif 7 < media < 9:
  print('Nasceu para programar!')
elif media > 9:
  print('Já pode ser chamado de Kanye, the dev, West!')
