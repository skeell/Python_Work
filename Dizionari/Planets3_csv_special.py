import csv


pianeti = []
pianeti_diz = {}

with open('planets.csv', 'r', encoding='utf-8') as infile:
    #infile.readline() #butta via la prima riga
    reader = csv.DictReader(infile)
    for pianeta in reader:
        #pianeti['massa'] = float(pianeti['massa']) #Nel caso volessi convertire il dato in float
        pianeti.append(pianeta)
        pianeti_diz['Planets'] = pianeta


print(pianeti)
print(pianeti_diz)

#maxg = 0
#nome_max = ''
#for pianeta in pianeti:
#    if pianeta['gravity'] > maxg:
#        nome_max = pianeta['nome']
#        maxg = pianeta['gravity']

#print(f'La massima gravità si trova sul pianeta {nome_max} e vale {maxg}')
