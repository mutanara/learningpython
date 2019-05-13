class Animal():
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body  "

    def get_color(self):
        return (self.color)
    
    def get_noise(self):
        return (self.noise)

obj = Animal()
obj.size = "small"
obj.color = "black"
obj.hair = "hairless"

print(obj.size)
print(obj.get_color())


class Dog(Animal): #this class Dog inherited features of parent class Animal, but it can also have it's own attributes. 
    name = "Jon"
    size = "small" # this is called "override" as this classs is having the same parameters with the parent class but with different variables.
    hair = "hairless"
instance = Dog()
instance.color = "white"
instance.name = "Jon Snow"

print(Dog.hair)
print(Dog.size)
print(Dog.name)
print(Dog.color)