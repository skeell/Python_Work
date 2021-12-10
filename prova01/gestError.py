# Leggere dei valori INTERI ed inserirli in una lista
# solo errori ValueError e IO Error
valori = []

dato = input("inserisci un dato: ")
while dato != '':
    try:
        d = int(dato)
        valori.append(d)
        dato = input("inserisci un dato: ")
    except ValueError as errore:
        print(f'il valore {dato} non è correttamente formattato!')
        print('Messaggio di errore: --> ', str(errore))
        dato = input("inserisci il dato: ")


print(valori)


