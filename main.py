from Student import Student
from Address import Address
from Car import Car

if __name__ == '__main__':
    st1 = Student("Ольга", 23, "1A")
    st2 = Student("Вася", 22, "1A")
    st3 = Student("Петя", 24, "2B")
    print(f"{st1}\n{st2}\n{st3}")
    print(st1.get_gender())

    car1 = Car("232", "Mers", "Белый", 260)
    car2 = Car("123", "BMW", "Черный", 170)
    car3 = Car("931", "Lada", "Серый",100)
    print(f"{car1}\n{car2}\n{car3}")

    address1 = Address("Ростов", "Социалистическая", "141")
    address2 = Address("Азов", "Ленина", "100")
    address3 = Address("Батайск", "Фрунзе", "50")
    print(f"{address1}\n{address2}\n{address3}")