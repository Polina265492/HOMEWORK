def days_indexes(self, day):
    day = f" Today the {day} of {self.name}'s life "
    print(f"{day:=^50}","\n")
    human_indexes = self.name + "'s indexes"
    print(f"{human_indexes:^50}","\n")
    print(f"Money – {self.money}")
    print(f"Satiety – {self.satiety}")
    print(f"Gladness – {self.gladness}")
    home_indexes = "Home indexes"
    print(f"{home_indexes:^50}", "\n")
    print(f"Food – {self.home.food}")
    print(f"Mess – {self.home.mess}")
    car_indexes = f"{self.car.brand} car indexes"
    print(f"{car_indexes:^50}", "\n")
    print(f"Fuel – {self.car.fuel}")
    print(f"Strength – {self.car.strength}")

    self.days_indexes(day)
    dice= random.randint
    if self.safiety < 20:
        print("Ill go eat!")
        self.eat()
    elif self.gladness <20:
        if self.home.mess > 15:
            self.home.clean()
        else:
            print("Tims chill")
            self.work()
    elif self.car.strenght < 15:
        print ("I nees to repair my car!")
        self.to_repair()
    if dice == 1
        print ('start working!')
        self.work
    elif dice == 3
        print('Cleaning time!')
        self.clean.home()
    elif dice == 4
        print ("Time for treats")
        self.shopping(manage ='delicacies')

nick = Human(name="Nick")
for day in range(1,365):
    if nick.live(day) == False:
        break
class House:
