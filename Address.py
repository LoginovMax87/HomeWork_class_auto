class Address:
    def __init__(self, city, street, house):
        self.__city = city
        self.__street = street
        self.__house = house

    def __str__(self):
        return (f"Адрес: г.{self.__city}, ул.{self.__street}, д.{self.__house}")


if __name__ == '__main__':
    Adddres1 = Address("Ростов", "Социалистическая", "141")
    print(Adddres1)