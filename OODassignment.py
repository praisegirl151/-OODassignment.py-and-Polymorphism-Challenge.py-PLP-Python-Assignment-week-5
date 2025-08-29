# smartphone.py

# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.storage}GB, Battery: {self.battery}%"


# Derived class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 20:
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system!")
            self.battery -= 20
        else:
            print(f"⚠️ Battery too low to play {game}. Please charge your phone.")

    # Polymorphism: overriding the charge method
    def charge(self, amount):
        super().charge(amount)
        print(f"{self.brand} {self.model} charges faster due to gaming mode ⚡")


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "S22", 256, 50)
    gaming_phone = GamingPhone("Asus", "ROG 6", 512, 30, "Liquid Cooling")

    print(phone1)
    phone1.make_call("08123456789")
    phone1.charge(40)

    print("\n" + str(gaming_phone))
    gaming_phone.play_game("PUBG")
    gaming_phone.charge(50)
