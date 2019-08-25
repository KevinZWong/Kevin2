
#Class definition
class Person:
	def __init__(self, name, birth_year, death_year):
		self.name = name
		self.birth_year = birth_year
		self.death_year = death_year

	def age(self):
		print('in')
		if 2016 < int(self.death_year):
			print('Alive')
			return 2016 - int(self.birth_year)
		else:
			print('Dead')
			return int(self.birth_year) - int(self.death_year)


#Usage:
johnObj = Person('John', '2000', '3000')
ageYear = johnObj.age()
print('John is ' + str(ageYear) + ' old')

joeObj = Person('Joe', '1900', '1980')
ageYear = joeObj.age()
if (ageYear < 0):
	print('Joe is dead at age ' + str(ageYear) + ' old')

