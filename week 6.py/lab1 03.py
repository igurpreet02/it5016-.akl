class car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year

    def detail(self):
        print(f"{self.color}")
    def models(self):
        print(f"{self.model}")
    def years(self):
        print(f"{self.year}")

car1=car("black","tesla model s",2023) 
car1.detail()
car1.models()
car1.years()  