class car:
    def __init__(self,color,model,car_name):
        self.color=color
        self.model=model
        self.car_name=car_name

    def driving(self):
        print(f"the {self.color}{self.car_name} is driving.")
    def stop(self):
        print(f"the {self.color}{self.car_name} is stopped.")
    def car_info(self):
        print(f"{self.model} {self.color} {self.car_name}")

car1=car("blue",2021,"ford mustang")
car1.driving()
car1.stop()
car1.car_info()