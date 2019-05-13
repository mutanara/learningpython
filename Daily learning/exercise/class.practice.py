#  Class Objects (obj and instance)

# 1

class Dog():
    name = "Jon"
    color = "brown"

instance = Dog()
obj = Dog()

print(instance.name)
print(obj.color)


#2: assigning a different variable to an object
obj.name = "Amber" 


print(obj.name)
print(instance.name) #this didn't change tho the obj.name has taken a new variable. for it to change on both of them, you would have to write instance = obj = Dog() on line 7.