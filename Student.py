class Student:
    def __init__(self, name, age, group):
        self.__name = name
        self.__age = age
        self.__group = group


    def __str__(self):
        return (f"Студент: {self.__name}, возраст: {self.__age}, группа: {self.__group}, пол: {self.get_gender()}")

    def get_gender(self):
        if self.__name.lower().endswith(("а")):
            return "Женский"
        return "Мужской"


if __name__ == "__main__":
    st1 = Student("Вася", 21, "52")
    print(st1)
