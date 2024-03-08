class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print("initialization {0}".format(self.name))
        Robot.population +=1
    def __init__(self):
        print("{self.name} destroyed")
        Robot.population -= 1
        if Robot.population ==0:
            print("{self.name} was last")
        else:
            print("still {0} robots".format(Robot.population))
            
            
    def say_hi(self):
        print("hello! my name is {0}".format(self.name))
        
    def how_many():
        print("this plane has {0} robots".format(Robot.population))
        
droid1 = Robot("R2-D2")
Robot.how_many()
droid2 = Robot("C-3PO")
Robot.how_many()