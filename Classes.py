#  -*- coding: UTF-8 -*-
from pprint import pprint as pp
from random import randint


class Car(object):

    def __init__(self, price, mileage_on_tachograph, engine_type, gasoline_tank, money_spent, max_mileage,
                 rate_per_hundred, price_of_overhaul, distance, utilization, delta):
        self.price = price
        self.mileage_on_tachograph = mileage_on_tachograph
        self.engine_type = engine_type
        self.gasoline_tank = gasoline_tank
        self.money_spent = money_spent
        self.max_mileage = max_mileage
        self.rate_per_hundred = rate_per_hundred
        self.price_of_overhaul = price_of_overhaul
        self.distance = distance
        self.utilization = utilization
        self.delta = delta


    def drive(self):
        if self.utilization == False:
            self.distance = randint(55000, 286000)
            if self.distance >= self.max_mileage:
                self.money_spent = self.price_of_overhaul*(self.distance//self.max_mileage)
        return self.distance

    def mileage(self):
        self.mileage_on_tachograph += self.distance
        return self.mileage_on_tachograph

    def residual_value(self):
        length_in_thousand_km = self.mileage_on_tachograph // 1000
        for i in range(0, length_in_thousand_km):
            self.price -= self.delta
        return self.price

    def how_much_fuel(self):
        fuel_in_litres = (self.distance/100)*self.rate_per_hundred
        return fuel_in_litres

    def how_many_refills(self):
        count_of_refills = self.distance//((self.gasoline_tank/self.rate_per_hundred)*100)
        return count_of_refills

    def rate_per_hundred(self):
        length_in_thousand_km = self.mileage_on_tachograph // 1000
        for i in range(0, length_in_thousand_km):
            self.rate_per_hundred += 0.01 * self.rate_per_hundred
        return self.rate_per_hundred

    def to_utilization(self):
        self.utilization = True
        return self.utilization

    def __str__(self):
        return({self.__dict__})


class PetrolCar(Car):
    def __init__(self):
        Car.__init__(self, price=10000, mileage_on_tachograph=0, engine_type='petrol',gasoline_tank=60,
                     money_spent=0, max_mileage=100000, rate_per_hundred=8, price_of_overhaul=500,
                     distance=0, utilization=False, delta=9.5)


class DieselCar(Car):
    def __init__(self):
        Car.__init__(self, price=10000, mileage_on_tachograph=0, engine_type='diesel', gasoline_tank=60,
                     money_spent=0, max_mileage=150000, rate_per_hundred=6, price_of_overhaul=700,
                     distance=0, utilization=False, delta=10.5)


if __name__ == '__main__':

    list_of_cars = []
    for i in xrange(100):
        if i % 3 == 0:
            a_car = DieselCar()
            a_car.drive()
            a_car.mileage()
            a_car.residual_value()
            list_of_cars.append(a_car)
        else:
            a_car = PetrolCar()
            a_car.drive()
            a_car.mileage()
            a_car.residual_value()
            list_of_cars.append(a_car)

    cars_mileage_list = map(lambda x: x.price, list_of_cars)
    print(cars_mileage_list)
    # a = PetrolCar()
    # b = DieselCar()
    # a.drive()
    # pp(a.__dict__)
    # cars_mileage_list = map(lambda x: x.mileage, Car.all_cars())
