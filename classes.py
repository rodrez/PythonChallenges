# Learning Classes

# Simple Class
# By convention we use CapitalCasing to name classes
class Sample():
    pass

# Creates an instance of the class
# An instance of the Class means when you assign a the Class to a variable
# Note how instead of variable assignment is called Class Instantiation
my_sample = Sample()

# If we check the type of our my_sample we should see that is a Sample type

print(type(my_sample))
# Output: <class '__main__.Sample'>

# Less Simple Class - Dog Class __init__ -> is a constructor of the Class and it will be called automatically when
# you create an instance of the class
#
# self -> represent the instance of the object itself. (self can be any word, however, it is good practice to keep
# the word self )
#
# breed argument -> We can see breed 3 times in the code block below. By convention is good to keep the words the same
# for readability purpose. Now if we take the breed argument and change to mybreed, and change the value of self.breed
# to mybreed, when you create the instance of the Dog class instead of passing a parameter called breed, we would pass
# a parameter called mybreed.
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

my_dog = Dog(breed='Huskie',  name='Fido', spots=5)

# NOTE: It is good practice to add some type of documentation with the data types that are expected for each argument.
# That way when another person looks at the code they would be able to understand which data type should be passed in.

my_dog.breed
my_dog.name
my_dog.species
my_dog.spots