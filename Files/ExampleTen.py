# Class definition
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


# Derived class (inheritance)
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Object instantiation
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Method invocation
print(dog.name + ": " + dog.speak())
print(cat.name + ": " + cat.speak())