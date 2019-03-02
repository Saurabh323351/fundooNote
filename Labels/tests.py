from django.test import TestCase

# Create your tests here.



def my_decorator(func):

    def inner(name):
        if name=='saurabh':
            print('hello','Dear','Saurabh')

        else:
            func(name)
    return inner

@my_decorator
def try_it(name):
    print('Hello',name)



try_it("rajat")
try_it("saurabh")
try_it("shubham")
