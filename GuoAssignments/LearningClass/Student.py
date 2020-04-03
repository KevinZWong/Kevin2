class Student:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, FirstName, LastName, Age, Gender):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Gender = Gender
    
    
    def displayFirstName(self):
        print("First Name: ", self.FirstName)

    def displayLastName(self):
        print("Last Name: ", self.LastName) 

    def displayAge(self):
        print("Age: ", self.Age) 

    def displayGender(self):
        print("Gender: ", self.Gender) 
    
    def displayFullName(self):
        print("Full Name", self.FirstName + " " + self.LastName)


            

Student1 = Student("Manni", "Evans", "213213", "Male")
Student2 = Student("Bob", "Yeet", "21321324343", "Male")
Student3 = Student("Jenny", "Hhersy", "214214", "Female")

Student1.displayFirstName()
Student1.displayLastName()
Student1.displayAge()

Student3.displayFirstName()
Student2.displayFullName()

#print("Total Students %d" % Students.SCount)