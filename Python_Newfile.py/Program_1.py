class Character:
    def __init__(self, name, weapon, health=100):
        self.name = name
        self.weapon = weapon
        self.health = health


    def attack(self):
        print(f"--- Character Status ---")
        print(f"Name   : {self.name}")
        print(f"Weapon : {self.weapon}")
        print(f"Health : {self.health}")
        print(f"{self.name} is attacking with {self.weapon}!")
        print("-" * 30)

if __name__ == "__main__":
    
    karna = Character("Karna", "Bow and Arrow")
    arjun = Character("Arjun", "Gandiva")

    
    arjun.attack()
    karna.attack()
