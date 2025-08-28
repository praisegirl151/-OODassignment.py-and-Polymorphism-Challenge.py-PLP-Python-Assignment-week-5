class Animal:
    def move(self):
        pass  # Abstract action


class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on land.")


class Fish(Animal):
    def move(self):
        print("🐟 The fish swims in water.")


class Bird(Animal):
    def move(self):
        print("🐦 The bird flies in the sky.")


# Polymorphism in action
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
