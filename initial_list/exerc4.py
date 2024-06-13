arthurm = int(input())
luizm = int(input())
pedrom = int(input())
h = int(input())

maxval = max(arthurm, luizm, pedrom)
minval = min(arthurm, luizm, pedrom)

maximum = ((maxval + minval +(abs(maxval - minval)))//2)*h

print(maximum)