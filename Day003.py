class Animal:
    animal_name = []

    @classmethod
    def AnimalFeatures(cls, name):
        if name in ['cow', 'sheep', 'goat']:
            return 4
        else:
            return 'not identified'

    def display(self):
        print("INFORMATION ABOUT ANIMAL:")
        name = input("Enter the name of the animal: ")
        legs = Animal.AnimalFeatures(name)
        return f"{name} has {legs} legs."

Animal.animal_name = ["cow", "donkey", "turkey", "hen"]
p1 = Animal()

result = p1.display()
print(result)

"""
static method, ti make any method a static one should put this keyword '@statcmethod' at the top
of the method name, Note: classmethod is a method that is bound to the class and not the instance of the class.
and it take cass itself as an argument which is convetionally name as 'cls'
"""