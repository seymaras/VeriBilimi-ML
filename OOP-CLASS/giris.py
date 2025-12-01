class Person():
    name=""
    age=0
    job=""
    gender=""

    def __init__(self,name,age,job,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printName(self):
        print(self.name)

mehmet = Person("Mehmet",24,"Developer","Male")
mehmet.printName()