while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Entrer une age valide !!")

if age >= 0 and age <= 12:
    print("Enfant")
elif age >= 13 and age <= 17 :
    print("Adolescent")
elif age >=18 and age <= 64:
    print("Adult")
else:
    print("Senior")