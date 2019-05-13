# CLASS methods a.k.a class' fucntions.

class Dog():
    name = "Jon"
    color = "brown"

    def get_color(self):
        return (self.color)
    
    def get_name(self):
        return (self.name)

instance = Dog()
obj = Dog()

print(obj.get_color())
print(obj.get_name()) #way of calling the class method

obj.color = "black" #this will as well change the obj.get_color

print(obj.get_color())