contacts = []
print("========= Carnet d'adress ==========")
print("1. Ajouter un contact a une liste")
print("2. Afficher tous les contacts")
print("3. Quitter le programme")
while True:
    try:
        choix = int(input("Entrer votre choix : "))
    except ValueError:
        choix = -1
    match choix:
        case 1:
            contact = input("Entrer Contact: ")
            contacts.append(contact)
        case 2:
            for contact in enumerate(contacts):
                print(f"{contact[0]}: {contact[1]}")
        case 3:
            print("Quittons....")
            break
        case _:
            print("Entrer une valeur valide!!!")
