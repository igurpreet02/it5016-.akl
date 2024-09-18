class car:
    def __init__(self,color,model,car_name):
        self.color=color
        self.model=model
        self.car_name=car_name

    def driving(self):
        print(f"the {self.color} {self.car_name} is driving.")
    def stop(self):
        print(f"the {self.color} {self.car_name} is stopped.")
    def car_info(self):
        print(f"{self.model} {self.color} {self.car_name}")

class Electriccar(car):
    def __init__(self, color, model, car_name,batterycapacity):
        super().__init__(color, model, car_name)
        self.batterycapacity=batterycapacity
        print(f"battery capacity: {self.batterycapacity} KWH")

myelectriccar=Electriccar("White", 2022,"tesla model 3",75)
myelectriccar.driving()
myelectriccar.stop()
myelectriccar.car_info()