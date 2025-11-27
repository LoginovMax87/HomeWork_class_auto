class Car:
    def __init__(self, number, model, color, power):
        self.__number = number
        self.__model = model
        self.__color = color
        self.__power = power

    def __str__(self):
        return (f"Авто: {self.__model}, номер: {self.__number}, цвет: {self.__color}, "
                f"мощность: {self.__power} л.с.\n"
                f"Утильсбор: {self.util_tax()} руб., "
                f"Транспортный налог: {self.transport_tax()} руб.")

    def util_tax(self):
        if self.__power <=159:
            return 5000
        elif 160<=self.__power <=250:
            return 200000
        else: return 100000000

    def transport_tax(self):
        if self.__power <=149:
            return self.__power * 10
        elif 150<=self.__power <=249:
            return self.__power * 20
        else: return self.__power * 30


if __name__ == '__main__':
    car1 = Car("12321", "BMW", "Red", 340)
    print(car1)