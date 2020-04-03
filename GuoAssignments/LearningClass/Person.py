class Person:
    def __init__(self, FirstName, LastName, IQ, HairColor, Gender):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IQ = IQ
        self.HairColor = HairColor
        self.Gender = Gender
        self.EyeColor = EyeColor
        self.Height = Height

    def displayFirstName(self):
        print("First Name: ", self.FirstName)

    def displayLastName(self):
        print("Last Name: ", self.LastName) 

    def displayAge(self):
        print("Age: ", self.Age) 

    def displayGender(self):
        print("Gender: ", self.Gender) 
    
    def displayFullName(self):
        print("Full Name:", self.FirstName + " " + self.LastName)

    def displayIQ(self):
        print("IQ: ", self.IQ) 

    def displayEyeColor(self):
        print("EyeColor: ", self.EyeColor) 

    def displayHeight(self):
        print("Height: ", self.Height) 

    