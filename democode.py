#Task7.6
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age <= 0:
            age is 0
            print("Age is not valid, setting age to 0")

        elif age < 13:
            print("You are young.")

<<<<<<< HEAD
        elif 13 <= age < 19:
            print("You are a good teenager.")
=======
        elif 13 <= age < 20:
            print("You are not just a teenager.")
>>>>>>> 4e73ec681656dff2e2c672932c4ebf89070552c5

        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        return age+1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
