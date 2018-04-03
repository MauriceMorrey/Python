class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -=1
        print "Health has decreased by 1"
        return self

    def run(self):
        self.health -= 5
        print "Health has decreased by 5"
        return self

    def display_health(self):
        print "Animal name is " + str(self.name)
        print "Current health is " + str(self.health)
        return self

animal1 = Animal("cat",25)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name,150)
        self.health = 150

    def pet(self):
        self.health += 10
        print "I am a good dog"
        return self

animal2 = Dog("Nala")
animal2.walk().walk().walk().run().run().display_health().pet()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name,170)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

animal3 = Dragon("Toothless")
animal3.walk().fly().display_health()
#animal3.pet = returns error because dragon doesn't have method pet

#animal4 = Dog("Kit")
#animal4.fly().display_health() = returns error because dog doesn't have method fly 
        
        
