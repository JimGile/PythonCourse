class RobotDog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof Woof!')


my_dog = RobotDog('Spot', 'Shepard')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
