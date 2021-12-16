pianeti = []
pianeti_diz = {}

with open('planets.csv', 'r', encoding='utf-8') as infile:
    infile.readline() #butta via la prima riga
    for line in infile:
        campi = line.rstrip().split(',')
        pianeta = {
            'nome' : campi[0],
            'massa' : float(campi[1]),
            'gravity' : float(campi[4])
        }

        pianeti.append(pianeta)
        pianeti_diz[campi[0]] = pianeta


print(pianeti)
print(pianeti_diz)

# Determinare quale pianeta ha la massima gravità

maxg = 0
nome_max = ''
for pianeta in pianeti:
    if pianeta['gravity'] > maxg:
        nome_max = pianeta['nome']
        maxg = pianeta['gravity']

print(f'La massima gravità si trova sul pianeta {nome_max} e vale {maxg}')

