qtd_veiculos = int(input())
acidente = input()
distancia_total = float(input())
cod_serializacao = input()

print('Análise das opções de transporte até o show!')

# Opcao A
tempo_a = ((distancia_total*0.8)/1089)*60 + ((distancia_total*0.2)/60)*60 + (0.6*qtd_veiculos)
if acidente == 'sim':
  tempo_a += 20
print(f'Opção A - Você chegará ao show em {int(tempo_a * 10) / 10} minutos')

# Opcao B
tempo_b = (distancia_total/40)*60 + 0.6 * qtd_veiculos
if acidente == 'sim':
  tempo_b += 20
print(f'Opção B - Você chegará ao show em {int(tempo_b * 10) / 10} minutos')

# Opcao C
tempo_c = 5 * (distancia_total / 60) * 10
print(f'Opção C - Você chegará ao show em {int(tempo_c * 10) / 10} minutos')

print('---')

# Codigo
cod_final = ''

for x in cod_serializacao:
  if int(x)%2 == 0:
    cod_final += x+'23'
  else:
    cod_final += x+'78'
print(f'Senha de serialização transformada: {cod_final}, guarde com segurança!')

    