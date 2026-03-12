from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    def __init__(self, prix, nomBoisson):
        self.prix = prix
        self.nomBoisson = nomBoisson
    @abstractmethod
    def cout(self):
        pass
    @abstractmethod
    def description(self):
        pass
    def afficheMenu(self):
        print("Commande:", self.description())
        print("Prix:",self.cout(),"€")

    def __add__(self, autre):
        return Menu(self, autre)
    

class Menu(Boisson):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def cout(self):
        return self.a.cout() + self.b.cout()

    def description(self):
        return self.a.description() +", " + self.b.description()


class Cafe(Boisson):
    def __init__(self, prix=2.0, nomBoisson="Cafe Simple"):
        super().__init__(prix, nomBoisson)
    def cout(self):
        return self.prix
    
    def description(self):
        return self.nomBoisson

class The(Boisson):
    def __init__(self, prix=1.5, nomBoisson="The"):
        super().__init__(prix, nomBoisson)
    def cout(self):
        return self.prix
    
    def description(self):
        return self.nomBoisson
    
class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

# ajoute de lait
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    def description(self):
        return self._boisson.description() + ", Lait"
# ajoute de Sucre
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
    def description(self):
        return self._boisson.description() + ", Sucre"
# ajoute de Caramel
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.75
    def description(self):
        return self._boisson.description() + ", Caramel"

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int

class Commande:
    def __init__(self, client, boissons=None):
        self.client = client
        self.boissons = boissons if boissons else []
    def ajouteBoisson(self, boisson):
        self.boissons.append(boisson)
    def calculePrixTotal(self):
        total = 0.0
        for boisson in self.boissons:
            total += boisson.cout()
        return total
    def afficheCommande(self):
        print("Command: ")
        for boisson in self.boissons:
            print(boisson.description(), end=", ")
        print("Prix Total:",self.calculePrixTotal())


class CommandeSurPlace(Commande):
    def __init__(self, client, boissons):
        super().__init__(client, boissons)
    def afficheCommande(self):
        print("Command Sur Place: ")
        for boisson in self.boissons:
            print(boisson.description(), end=", ")
        print("\n")
        print("Prix Total:",self.calculePrixTotal())

class CommandeEmporter(Commande):
    def __init__(self, client, boissons):
        super().__init__(client, boissons)
    def afficheCommande(self):
        print("Command Emporter: ")
        for boisson in self.boissons:
            print(boisson.description(), end=", ")
        print("Prix Total:",self.calculePrixTotal())

class Fidelite:
    def ajouterPoints(self, client):
        client.points_fidelite += 1

class CommandeFidele(Commande, Fidelite):
    def __init__(self, client, boissons=None):
        super().__init__(client, boissons)
    def applyDiscount(self):
        for boisson in self.boissons:
            self.ajouterPoints(self.client)


caffe = Cafe()
caffe = Lait(caffe)
caffe = Sucre(caffe)

the = The()

caffe2 = Cafe()
caffe2 = Caramel(caffe2)

client = Client("yassine", 1, 0)

commande = Commande(client)
commande.ajouteBoisson(caffe)
commande.ajouteBoisson(the)
commande.ajouteBoisson(caffe2)

commande.afficheCommande()

print("Points avant :", client.points_fidelite)

commande_fidele = CommandeFidele(client, commande.boissons)
commande_fidele.applyDiscount()

print("Points après :", client.points_fidelite)



