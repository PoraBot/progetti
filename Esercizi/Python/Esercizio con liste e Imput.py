def tclass ():
    
    tlist = [ "Sandy" , "Fabio" , "Matteo"]
    
    nome1 = input("Inserici un nome da aggiungere alla lista:\n")
    if nome1.isnumeric():
        print("Si prega di inserire un nome")
    else:
        print(f"Hai aggiunto {nome1} alla lista")
        tlist.append(nome1)
    
    nome2 = input("Inserici un secondo nome da aggiungere alla lista:\n")
    if nome2.isnumeric():
        print("Si prega di inserire un nome")
    else:
        print(f"Hai aggiunto {nome2} alla lista")
        tlist.append(nome2)
    
    print(f"La lista completa è : " + str(tlist))
    
#tclass()

def esercizio_try():
    stringa = input('Inserisci un numero: ')
    try:
        intstr = int(stringa)
    except:
        intstr = -1

    if intstr > 0:
        print('Hai inserito un numero')
    else:
        print('Inserisci un numero ')

esercizio_try()

# Per la conversione si usano le funzioni tipo float(), str(), int() etc.. ma possiamo controllare il tipo
# di una variabile 