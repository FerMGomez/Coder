from multiprocessing.context import assert_spawning
from re import S
import ssl
from this import d


class Vehicle():
    def __init__(self, color, brand, model, year):
        self.color = color
        self.brand = brand
        self.model = model 
        self.year = year

    def prin_data (self):
        print(f"color: {self.color}")
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
    
    def run(self):
        print('Vehicle is running')

class Car(Vehicle):
    def  run(self):
        print('Car is running')
# Algo que pueda hacer un automovil que la moto no pueda realizar
    def run_backwards(self):
        print('Car is running backwards')

class Motorcycle(Vehicle):
    def __init__(self, color, brand, model, year,casco):
        super().__init__(color, brand, model, year)
        self.casco = casco
    def run(self):
        print('Motorcycle is running')
# Algo que pueda hacer la  motocicleta que el automivil no pueda realizar
    def do_a_wheelie(self):
        print('Motorcycle is doing a wheelie')

print('-------- Car ---------/n')
Car_1 = Car('A','AA','AAA','AAAA')
Car_1.prin_data()
Car_1.run()
Car_1.run_backwards()


print('-------- Moto ---------/n')
Motorcycle_1 = Motorcycle('B','BB','BBB','BBBB','BBBTY')
Motorcycle_1.prin_data()
print(Motorcycle_1.casco)
Motorcycle_1.run()
Motorcycle_1.do_a_wheelie()
assert_spawning

d
ssl
S
S
S
