
def main():
    ciccio = cripta('pippo.txt')
    print(ciccio)
    cacchio = decript(cripta('pippo.txt'))




def cripta(filein):
    # Dopo aver inserito e letto un testo
    # Questo viene criptato
    cript = []
    for elem in filein:
        car = ord(elem)
        cript.append(car)

    return cript




def decript(file):
    decr= []
    for elem in filein:
        car = ord(elem)
        decr.append(car)




main()
