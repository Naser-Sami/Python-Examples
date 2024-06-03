

# APPROACH #1 - Singleton2() method
#
# Client code uses Singleton2() to create AND access the Singleton2 instance,
# which is the standard way in which an object is created.  This makes it more 
# implicit that Singleton2 is in fact a Singleton object... the writer of the 
# client code might not be aware that Singleton2 is a singleton (perhaps it is
# not in the name of the class as it is here), and may expect that Singleton2() 
# returns a new object each time it is used as would normally be expected!
#


class Singleton:
    # class variable __instance will keep track of the lone object instance
    __instance = None

    # A magic method / dunder method that is called when we create a Singleton2 
    # object with Singleton2().  We have it check the __instance class variable 
    # to see if the instance has been created, if it hasn't, we create it, and 
    # whether we needed to create it or not we return the instance.
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = \
            super(Singleton, cls).__new__(cls)
        return cls.__instance
    

# We can just create the Singleton2 objects in the usual way, but it is only 
# ever going to be the same object that is returned as s1 = s2!
s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
print(s1 == s2)


# again if we set an attribute on s1, s2 will have the same value because they 
# both refer to the same object
s1.x = 10
print(s2.x)
