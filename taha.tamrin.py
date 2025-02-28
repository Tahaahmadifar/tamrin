import random 

#singel inheritance

class Aclass():
    def __init__(self, start_randint, stop_randint):
        self.start_randint = start_randint
        self.stop_randint = stop_randint
        return self.start_randint,self.stop_randint

    def random_value(self, start_randint, stop_randint):
        random_number = random.randint(start_randint, stop_randint)
        print(random_number)
        return random_number

class Bclass(Aclass):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint,stop_randint)

    def final_method(self):
        start_randint,stop_randint = self
        result_var = self.random_value(self.start_randint, self.stop_randint)
        while True:
            try:
                gusse_value = int(input("Please enter your guess: "))
                if gusse_value > 10:
                    print("Please enter number between 1 & 10")
                elif result_var == gusse_value:
                    print("***True***")
                    break
                else:
                    print("False, try again!!")
            except ValueError:
                print("Please enter integer only")

object1 = Bclass(1,10)
object1.final_method()

#Multiple inheritance

class Aclass():
    def define_value(self):
        start_randint = 1
        stop_randint = 10
        return start_randint,stop_randint

class Bclass():
    def random_value(self, start_randint, stop_randint):
        random_number = random.randint(start_randint,stop_randint)
        print(random_number)
        return random_number

class Cclass(Aclass,Bclass):
    def final_method(self):
        start_randint, stop_randint = self.define_value()
        result_var = self.random_value(start_randint, stop_randint)
        while True:
            try:
                gusse_value = int(input("Please enter your guess: "))
                if gusse_value > 10:
                    print("Please enter number between 1 & 10")
                elif result_var == gusse_value:
                    print("***True***")
                    break
                else:
                    print("False, try again!!")
            except ValueError:
                print("Please enter integer only")

object1 = Cclass()
object1.final_method()

#Multilevel inheritance

class level1():
    def __init__(self, start_randint, stop_randint):
        self.start_randint = start_randint
        self.stop_randint = stop_randint

    def define_value(self):
        return self.start_randint, self.stop_randint

class level2(level1):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint, stop_randint)

    def random_value(self):
        random_number = random.randint(self.start_randint, self.stop_randint)
        print(random_number)
        return random_number

class level3(level2):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint, stop_randint)

    def final_method(self):
        result_var = self.random_value()

        while True:
            try:
                gusse_value = int(input("Please enter your guess: "))
                if gusse_value > 10:
                    print("Please enter number between 1 & 10")
                elif result_var == gusse_value:
                    print("***True***")
                    break
                else:
                    print("False, try again!")
            except ValueError:
                print("Please enter integer only")

object1 = level3(1, 10)
object1.final_method()

#Hybrid inheritance

class Aclass():
    def __init__(self, start_randint, stop_randint):
        self.start_randint = start_randint
        self.stop_randint = stop_randint

    def define_value(self):
        return self.start_randint, self.stop_randint

class Bclass(Aclass):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint, stop_randint)

    def random_value(self):
        random_number = random.randint(self.start_randint, self.stop_randint)
        print(random_number)
        return random_number

class Cclass(Bclass):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint, stop_randint)

    def gusse_value(self):
        self.gusse_number = gusse_number
        return self.gusse_number

class Dclass():
    def number_rand(self):
        random_number = self.random_value()
        return random_number

class Eclass(Cclass,Dclass):
    def __init__(self, start_randint, stop_randint):
        super().__init__(start_randint, stop_randint)

    def final_method(self):
        result_var = self.number_rand()
        while True:
            try:
                gusse_value = int(input("Please enter your guess: "))
                if gusse_value > 10:
                    print("Please enter number between 1 & 10")
                elif result_var == gusse_value:
                    print("***True***")
                    break
                else:
                    print("False, try again!!")
            except ValueError:
                print("Please enter integer only")

object1 = Eclass(1,10)
object1.final_method()

#Random with decorator

def dec1(funk):
    def def_inner():
        random_number = random.randint(1,10)
        def_inner.random_number = random_number
        print(def_compare.random_number)
        return funk()
    return def_inner

@dec1
def def_compare():
    while True:
            try:
                gusse_value = int(input("Please enter your guess: "))
                if gusse_value > 10:
                    print("Please enter number between 1 & 10")
                elif def_compare.random_number == gusse_value:
                    print("***True***")
                    break
                else:
                    print("False, try again!!")
            except ValueError:
                print("Please enter integer only")

def_compare()

#Random with decorator & assert

import random

def dec1(funk):
    def def_inner():
        random_number = random.randint(1, 10) 
        
        def def_compare():
            while True:
                try:
                    guess_value = int(input("Please enter your guess: "))
                    assert random_number == guess_value, "False, try again!!"
                    print("***True***")
                    break 
                except AssertionError as aeg:
                    print(aeg)
                except ValueError:
                    print("Please enter an integer only.")

        def_compare()  
        return funk  
    return def_inner

@dec1
def def_compare():
    pass

def_compare()