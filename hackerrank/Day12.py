class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        avarage = 0
        for score in self.scores:
            avarage += score
        avarage = avarage/len(self.scores)
        
        if avarage >= 90 and avarage <= 100:
            return "O"
        if avarage >= 80 and avarage < 90:
            return "E"
        if avarage >= 70 and avarage < 80:
            return "A"
        if avarage >= 55 and avarage < 70:
            return "P"
        if avarage >= 40 and avarage < 55:
            return "D"
        if avarage < 40:
            return "T"
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

### input
# Heraldo Memelli 8135627
# 2
# 100 80