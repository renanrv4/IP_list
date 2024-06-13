x = int(input())
z = int(input())

dhm = ((34 - x)**2 + (220 - z)**2)**(1/2)
dkk = ((0 - x)**2 + (0 - z)**2)**(1/2)
ds = ((140 - x)**2 + (456 - z)**2)**(1/2)

print(f'Distancia para Hogsmeade: {dhm:.2f}')
print(f'Distancia para Kakariko: {dkk:.2f}')
print(f'Distancia para Solitude: {ds:.2f}')