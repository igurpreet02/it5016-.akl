class Car:
    def __init__(self,color,modul,):
        self.color=color
        self.modul=modul
    def drive(self):
        print(f"the {self.color}_{self.modul} is driving.")
    def stop(self):
        print(f"the {self.color}_{self.modul}has stopped")
    def not_working(self):
        print(f"the {self.color}_{self.modul} car is not working because its broken")
car1=Car("red", "ferrari")
car2=Car("blue", "subaru")
car3=Car("yellow","swift")

car1.drive()
car2.stop()
car3.not_working()