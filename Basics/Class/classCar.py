
# definition or blue-paint

class car:
    carType = ""
    year = ""
    engine = ""
    door = ""
    headlight = ""
    def __init__(self, carType, year, engine, door):
        self.carType = carType
        self.year = year
        self.engine = engine
        self.door = door
    def whatCarType(self):
        return self.carType

    def whatYear(self):
        return self.year 

    def whatEngine(self):
        return self.engine 

    def whatdoor(self):
        return self.door

    def whatheadlight(self):
        return self.headlight



# &&&&&&&&&&&&&&& Usage
Honda = car("Honda", "2001", "4 cycle", "4 door")
Type = Honda.whatCarType()
print("Type= ", Type)

Year = Honda.whatYear()
print("Year= ", Year)

Engine = Honda.whatEngine()
print("Engine= ", Engine)

door = Honda.whatdoor()
print("door= ", door)

print('headlights = 2 headlights')



Toyata = car("Toyata", "2003", "6 cycle", "5 door")
Type = Toyata.whatCarType()
print("Type= ", Type)

Year = Toyata.whatYear()
print("Year= ", Year)

Engine = Toyata.whatEngine()
print("Engine= ", Engine)

door = Toyata.whatdoor()
print("door= ", door)

print('headlights = 2 headlights')



Benz = car("Benz", "2011", "6 cycle", "2 door")
Type = Benz.whatCarType()
print("Type= ", Type)

Year = Benz.whatYear()
print("Year= ", Year)

Engine = Benz.whatEngine()
print("Engine= ", Engine)

door = Benz.whatdoor()
print("door= ", door)



Tesla = car("Tesla", "2015", "6 cycle", "5 door")
Type = Tesla.whatCarType()
print("Type= ", Type)

Year = Tesla.whatYear()
print("Year= ", Year)

Engine = Tesla.whatEngine()
print("Engine= ", Engine)

door = Tesla.whatdoor()
print("door= ", door)

Type = Honda.whatCarType()
print("Type= ", Type)

# $$$$$$$$$$$$$$$$$$$$$$$$$$

Year = Honda.whatYear()
print("Year= ", Year)

Year = Toyata.whatYear()
print("Year= ", Year)

Year = Benz.whatYear()
print("Year= ", Year)

Year = Tesla.whatYear()
print("Year= ", Year)