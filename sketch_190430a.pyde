from abc import ABCMeta, abstractmethod

class Pet():
    __metaclass__ = ABCMeta
    @abstractmethod
    def speak():
        return "no sound"
class Dog():
    def __init__(self, name):
        self.name=name
    def speak(self):
        return 'woof'
    def __sub__(self, other):
        return "psy odjete"
class Cat():
    def __init__(self, name):
        self.name=name
    def speak(self):
        return 'meow'
    def __add__(self, other):
        return "koty dodane"
class Patyczak(Pet):
    def __init__(self, name):
        self.name=name
    def speak(self):
        return "belmondo"
cola = Cat("Cola")
skrypcik = Cat("Skrypcik")
cezar = Dog("Cezar")
lucy = Dog("Lucy")
patyczak = Patyczak("Patyczak")
lista_zwierzat = [cola,skrypcik,cezar,lucy,patyczak]
for pet in lista_zwierzat:
    print(pet.speak())
#print(isinstance(cola, Pet))
print(cezar-lucy)
print(cola+skrypcik)
