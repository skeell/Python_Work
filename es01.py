'''
Scrivi una funzione che prende due numeri come parametro e 
manda in print il più grande tra i due.
Per quanto Python disponga di una funzione 
max(), sei invitato a utilizzare le 
istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
'''

#funzione di controllo
def controllo(a,b):
    if a == b:
        print("I due numeri sono identici")
    elif b > a:
        print("il più grande tra i due è " + str(b))
    else :
        a > b
        print (" il più grande tra i due è " + str(a))
   


# richiesta numeri 
primoNumero = int(input("dammi un numero"))
secondoNumero = int(input("dammi un altro numero"))
controllo (primoNumero, secondoNumero)
