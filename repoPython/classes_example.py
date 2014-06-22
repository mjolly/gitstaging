# In Python 2, inheriting from nothing results in an "old-style"
# class. If you ask this class for its type using the type built-in,
# it says "instance." Instead inherit from object (or from a built-in
# class, or an object that inherits from object). This results in a
# "new-style" class. In Python 3, all classes will be new-style.
class Orange(object): # Classes are named in CamelCase
    
    # Some classes have variables directly in them, but most classes
    # only have methods. A method has the exact same syntax as a
    # function, because ultimately all it is is a function with an
    # implicit first argument of the class instance it is bound to. By
    # convention this argument is "self". Note that the constructor is
    # just a method of the class, with a special name, "__init__", to
    # show that it is the constructor. So suppose I instantiate some
    # class like this
    #
    # my_berry1 = Strawberry('red', 'big')
    #
    # Python will look for the Strawberry.__init__ and if it doesn't
    # find it then it will look for it in its parent classes. Then it
    # will call it with THREE (not two) arguments. The first is the
    # new Strawberry instance it is creating, and the second is 'red',
    # and the third is big. So the signature of init should look like
    # this
    #
    # def __init__(self, 'red', 'big'):
    #
    # By convention, the __init__ special method, if defined, is
    # defined before other methods of the class.
    
    def __init__(self, color, peel_thk, is_peeled=False):
        # Four arguments in the constructor. The first one is the
        # instance and does not appear in the instantiation call. The
        # next two are required arguments, and the final one is
        # optional.
        
        self.color = color
        self.peel_thickness = peel_thk
        self.is_peeled = is_peeled
        self.shape = 'round'

    def peel(self):
        if self.is_peeled:
            print 'Already peeled.'
        else:
            print 'Peeled through ' + str(self.peel_thickness) + ' mm of skin'
            self.is_peeled = True

    def unpeel(self):
        raise NotImplementedError("I don't know how!")

    @property
    def has_skin(self):
        return not self.is_peeled

# This class inherits from Orange, so it gets all its methods,
# including __init__. Here I override peel with a new method that is
# specific to instances of BloodOrange. Everything else is the same.
class BloodOrange(Orange): # Inherit from Orange.
    def peel(self):
        print 'BloodOranges are invincible to peeling!'

        
# Instantiating with only the two required arguments.
orange1 = Orange('#fff888222', 0.3)
print orange1.is_peeled # prints False
print orange1.has_skin # prints True
orange1.peel() # prints "Peeled through 0.3 mm of skin"
print orange1.is_peeled # prints True
print orange1.has_skin # prints False

# Instantiating with the is_peeled argument as well.
orange2 = Orange('blue', 0.2, True) 
print orange2.is_peeled # prints True

# List comprehension. Go through every element in thickness_list,
# assign the element to x, then call Orange('red', x), and append the
# result to a list.
thickness_list = [0.1, 0.2, 0.3, 0.4]
oranges = [Orange('red', x) for x in thickness_list]
print oranges[2].peel_thickness # prints 0.3

# Make two new lists each with half the oranges. Note that I can use
# the same slice index in both of these lines only because of the
# whole "list indices refer to the spaces BETWEEN the elements" thing.
oranges_half1 = oranges[:len(oranges) / 2]
oranges_half2 = oranges[len(oranges) / 2:]
print [x.peel_thickness for x in oranges_half1] # prints [0.1, 0.2]
print [x.peel_thickness for x in oranges_half2] # prints [0.3, 0.4]

# Peel oranges if their skin is too thick.
for orange in oranges:
    if orange.peel_thickness >= 0.3:
        orange.peel()
print [x.has_skin for x in oranges] # prints [True, True, False, False]

# Instantiating the subclass.
orange3 = BloodOrange('blood_red', 0.1)
orange3.peel()
print orange2.is_peeled # prints False
orange3.unpeel()
