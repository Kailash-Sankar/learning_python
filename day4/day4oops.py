# inheritance

# object is provided to inherit from python object ( future proof)
class Animal(object):
    type = 'mammal'

    def walk(self):
        print("i am walking")


# inherit animal class
class Dog(Animal):
    def speak(self): print("such bow much wow")

    def likes(self): print("bones")

    def hunts(self): print("cats")


class Cat(Animal):
    def speak(self): print("meau..meau")

    def likes(self): print("milk")

    def playswith(self): print("jerry")


class Doat(Cat, Dog):  # order matters, first one gets priority
    def hobby(self): print("python programming")

    def speak(self): print("bow .. meau")

    def pspeak(self): super(Doat, self).speak()


tommy = Dog()
tommy.speak()
tommy.walk()

ginger = Doat()
ginger.speak()
ginger.likes()
ginger.hunts()
ginger.playswith()
ginger.hobby()
ginger.pspeak()

# class methods are also inherited
print(ginger.type)

# method resolution order
print(Doat.__mro__)
