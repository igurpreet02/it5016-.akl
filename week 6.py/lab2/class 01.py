class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")
MYDog = Dog("buddy")
MYDog.speak()
MYDog.bark()