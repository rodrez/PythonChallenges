class Dog():

    # CLASS OBJECT ATTRIBUTE -> is the same for any instance of the class.
    species = 'mammal'

    def __init__(self,breed,name, spots):

        # Attributes
        # We take the argument and assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expects a boolean/integer/etc.
        self.spots = spots

    # Methods are more like actions, it is basically a function(  a method is a function inside
    # a class that works with the object in some way).
    def bark(self, age):

        # Note: When passing an attribute it is important to use the self keyword, we need to use self to
        # to reference the particular instance of the attribute
        # Note: How when we passed age as an argument we did not use the self keyword. We do not use self
        # age is being provided by us when you call the bark method.
        print('Woof! My name is {} and my age is {}'. format(self.name, age))

my_dog = Dog('Huskie', 'Fido', spots=5)
print(my_dog.breed)
print(my_dog.species)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.bark(2))
