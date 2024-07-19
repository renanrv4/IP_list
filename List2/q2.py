n_pessoas = int(input())

aprovados = 0
reprovados = 0
abstencao = 0

taxa_aprovacao = 0
taxa_rejeicao = 0
taxa_abstencao = 0

# For Loop para registrar as respostas
for x in range(n_pessoas):
  resposta = input()
  if resposta == 'Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!':
    aprovados += 1
  elif resposta == 'Não gostei. Muito sem graça, onde já se viu nome com duas letras?':
    reprovados += 1
  else:
    abstencao += 1

taxa_aprovacao = (aprovados / n_pessoas)*100
taxa_rejeicao = (reprovados / n_pessoas)*100
taxa_abstencao = (abstencao / n_pessoas)*100

print('A pesquisa terminou e os resultados foram os seguintes:')
print(f'Taxa de aprovação: {taxa_aprovacao:.2f}')
print(f'Taxa de rejeição: {taxa_rejeicao:.2f}')
print(f'Taxa de abstenção: {taxa_abstencao:.2f}')

if taxa_aprovacao > taxa_rejeicao:
  print('YES!!! Sabia que as pessoas gostariam!')
elif taxa_rejeicao > taxa_aprovacao:
  print('Ops... Por essa eu não esperava.')
else: 
  print('Bom... Vou olhar para o copo meio cheio!')
 

  

