from Person import Person 

class Student2(Person):
    def __init__(self, FirstName, LastName, IQ, HairColor, Gender):
        super().__init__(FirstName, LastName, IQ, HairColor, Gender)


Student1 = Student2("Manni", "Evans", "213213", "Male", "123")
Student1.displayFullName()


class Teacher2(Person):
    def __init__(self, FirstName, LastName, IQ, HairColor, Gender):
        super().__init__(FirstName, LastName, IQ, HairColor, Gender)
Teacher1 = Teacher2("Creative", "Name", 10, "Black", "male")
Teacher1.displayFullName()

class Janitor(Person):
    def __init__(self, FirstName, LastName, IQ, HairColor, Gender):
        super().__init__(FirstName, LastName, IQ, HairColor, Gender)
Janitor1 = Janitor("VeryCreative", "Name", 10, "Black", "male")
Janitor1.displayFullName()
