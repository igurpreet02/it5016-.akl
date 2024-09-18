class person():
    #constructor
    def __init__(self,name,gender):
        self.name=name
        self.age=12
        self.gender=gender

    def speak(self):
        quote=input(f"what does the {self.name} says?:")

#object
person1=person("rashid","male")
person1=person("khanchna","female")
person()