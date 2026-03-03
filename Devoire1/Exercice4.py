while True:
    try:
        nbr1 = int(input("Entrer premier nombre: "))
        nbr2 = int (input("Entrer le dexieme nombre: "))
        print("1. addition\n2. soustraction\n3. multiplication\n4. division")
        operation = int(input("Choisire l'opperation: "))
        break
    except ValueError:
        print("Nombre ou operation invalide")

match operation:
    case 1:
        print(nbr1 + nbr2)
    case 2:
        print(nbr1 - nbr2)
    case 3:
        print(nbr1 * nbr2)
    case 4:
        try:
            print(nbr1 / nbr2)
        except ZeroDivisionError:
            print("Erreru : Essay de Division par 0")
    case _:
        print("Entrer une operation valide!!")