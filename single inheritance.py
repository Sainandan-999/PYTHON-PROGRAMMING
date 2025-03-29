class vehicle:
    def mov(self):
        print("the car is moving")
class car(vehicle):
    def honk(self):
        print("the car is honking")
my_car=car()
my_car.mov()
my_car.honk()

class engine:
    def start(self):
        print("engine is started")
class radio:
    def play_music(self):
        print("playing music")
class Car(engine,radio):
    pass
car=Car()
car.start()
car.play_music()