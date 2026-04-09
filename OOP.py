class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
         print(f"{self.name} is barking!")

    def change_name(self, new_name):
        self.name = new_name


jack = Dog(name="Buck", age=5, breed="Labrador")
captain =Dog(name="Capoon", age=3, breed="Golden Retriever") 

old_name = jack.name
jack.change_name("MAX")

print(f"{old_name} is now called {jack.name}")
