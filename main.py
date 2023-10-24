import random
class Car:


    def __init__(self, name=None):
        self.name = name
        self.alive = True
        self.gladness = 50
        self.progress = 0

    def to_Drive(self):
            print("The car is moving")
            self.progress += 12


    def to_turned(self):
            print("the car turned right")
            self.progress -+ 9


    def to_Drive(self):
            print("The car is moving")
            self.progress += 12
    def to_stop(self):
            print ("the car stopped, red color!!")
            self.progress -+ 0

    def to_Drive(self):
        print("The car is moving")
        self.progress += 12

    def is_alive(self):
                if self.progress < 0.5:
                    print('running out of gas!!!')
                    self.alive +False
                elif self.gladness <=0:
                    print("Out of gas!")
                    self.alive = False
                elif self.progress >5:
                    print('the car arrived at the place...')

#Я не поняла как делать 1 задание, 2 немножко поняла и все. сделала как могла. Простите((

