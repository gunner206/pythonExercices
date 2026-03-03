donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
]

def valider(record):
    raison = ""
    nom = record[0]
    matiere = record[1]
    groupe = record[3]
    try:
        if not record[2]:
            raise ValueError
        else:
            note = float(record[2])
    except ValueError:
        raison = raison + "Note non valide"
        return (False, raison)

    if not nom or not isinstance(nom, str):
        raison = raison + "Nom non valide invalide"
    elif not matiere or not isinstance(matiere, str):
        raison = raison + "Prenom non Valide"
    elif not groupe or not isinstance(groupe, str):
        raison = raison + "Groupe non valide"
    elif note > 20 or note < 0:
        raison = raison + "Note Non Valide"
    else:
        result = (True, raison)
        return result
    
    result = (False, raison)
    return result

def clean(data):
    filteredData = []
    for record in data:
        test = valider(record)
        if test[0] == True:
            filteredData.append(record)
    return filteredData

def getErrors(data):
    errors = []
    for record in data:
        test = valider(record)
        if test[0] == False:
            error = {"ligne" : record, "raison" : test[1]}
            errors.append(error)
    return errors

def calculeSum(matieres_dict ,keys_list):
    sum = 0
    if not keys_list:
        return 0
    current_matieres = keys_list[0]
    note = matieres_dict[current_matieres]
    return note + calculeSum(matieres_dict, keys_list[1:])
def calculeMoyenne(students):
    moyenneDict = {}
    for student, notes in students.items():
        keys = list(notes.keys())
        count = len(keys)
        total = calculeSum(notes, keys)
        moyenneDict[student] = round((total / count) * 100) / 100
    return moyenneDict
def analyseAnomalie(students, matieres):
    for student, notes in students.items():
        if len(notes) != len(matieres):
            print(f"Erreur: {student} n'as pas toute les notes!!")
        elif calculeMoyenne(students)[student] < 10:
            print("Erreur moyenne inferieur a 10")
        for note in notes:
            min = 0
            max = 0
            if (min > max)

    
    

def main():
    cleanData = clean(donnees)
    matieres = set()
    students = {}
    groupes = {}
    for data in cleanData:
        nome = data[0]
        matiere = data[1]
        note = data[2]
        groupe = data[3]
        # ajoute matiere
        matieres.add(matiere)
        # ajoute etudiant
        if nome in students:
            students[nome][matiere] = note
        else:
            studentInfo = {matiere : note}
            students[nome] = studentInfo
        if groupe in groupes:
            groupes[groupe].add(nome)
        else:
            groupes[groupe] = {nome}

    print(students)
    




if __name__ == "__main__":
    main()