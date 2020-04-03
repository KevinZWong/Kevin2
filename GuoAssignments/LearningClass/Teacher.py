class Teacher:
    def __init__(self, FirstName, LastName, IQ, HairColor, Gender):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IQ = IQ
        self.HairColor = HairColor
        self.Gender = Gender
   
    def displayFirstName(self):
        print("FirstName: ", self.FirstName) 

    def displayLastName(self):
        print("LastName: ", self.LastName) 

    def displayIQ(self):
        print("IQ: ", self.IQ) 

    def displayHairColor(self):
        print("HairColor: ", self.HairColor) 

    def displayGender(self):
        print("Gender: ", self.Gender) 


Teacher1 = Teacher("Creative", "Name", 10, "Black", "male")
Teacher1.displayGender()

