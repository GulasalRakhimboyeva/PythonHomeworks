class Animal:
    def __init__(self, name, age, colour  ):
        self.name = name
        self.age = age
        self.colour = colour

    def __str__(self):
        return f"{self.name} is {self.age} years old and it's colour is {self.colour}"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
class Dogs(Animal):
    def speak(self, sound="Vav-vav"):
        return super().speak(sound)
    def runs(self, speed):
        return f"{self.name} runs {speed} km/h."
class Cats(Animal):
    def speak(self, sound="miav-miav"):
        super().speak(sound)
    def sleep(self, hour):
        return f"{self.name} sleeps {hour} hours a day."
class Cows(Animal):
    def speak(self, sound="mo-mo"):
        super().speak(sound)
    def milk(self, milk):
        return f"{self.name} gives {milk} l milk a day."
class Birds(Animal):
    def speak(self, sound="chirp-chirp"):
        super().speak(sound)
    def fly(self, length):
        return f"{self.name} can fly {length} km away."
    

simba=Dogs("Simba", 23, "white")

print(simba.runs(23))
