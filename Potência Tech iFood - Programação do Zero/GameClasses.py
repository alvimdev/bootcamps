class Hero:
    def __init__ (self, name, age, role):  
        self.name = name
        self.__age = age
        self.role = role
        
    def getAge(self):
        return self.__age

    def attack(self, quirk):
        print(f'O {self.role}, {self.name}, atacou usando {quirk}')
        
def role_quirk(r):
    r = r.lower()
    if r == "Warrior".lower():
        return "Espada"
    elif r == "Mage".lower():
        return "Magia"
    elif r == "Monk".lower():
        return "Artes Marciais"
    elif r == "Ninja".lower():
        return "Shuriken"
    else:
        return "Pedras"
    
naruto = Hero("Narudo Uzumaki", 16, "Ninja")
macilio = Hero("Marcio", 20, "Servente de Pedreiro") # Meu querido grande pai em seus 20 anos de idade 

naruto.attack(role_quirk("ninja"))
macilio.attack(role_quirk("Pedreiro"))