from decimal import Decimal, getcontext

getcontext().prec = 15

qtd_veiculos = int(input())
acidente = input()
distancia_total = float(input())
codigo = input()

codigo_desserializado = ''

print('Análise das opções de transporte até o show!')

# Opcao A
tempo_a = ((distancia_total*0.8)/1089)*60 + ((distancia_total*0.2)/60)*60 + (0.6*qtd_veiculos)
ta = Decimal(tempo_a)
if acidente == 'sim':
  ta += 20
print(f'Opção A - Você chegará ao show em {ta:.1f} minutos')

# Opcao B
tempo_b = (distancia_total/40)*60 + 0.6 * qtd_veiculos
tb = Decimal(tempo_b)
if acidente == 'sim':
  tb += 20
print(f'Opção B - Você chegará ao show em {tb:.1f} minutos')

# Opcao C
tempo_c = 5 * (distancia_total / 60) * 10
tc = Decimal(tempo_c)
print(f'Opção C - Você chegará ao show em {tc:.1f} minutos')

for x in codigo:
  if int(x)%2 == 0:
    codigo_desserializado += x+'23'
  else:
    codigo_desserializado+= x+'78'

print('---')
print(f'Senha de serialização transformada: {codigo_desserializado}, guarde com segurança!')
