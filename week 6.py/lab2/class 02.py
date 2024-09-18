class Vehical:
    def __init__(self) -> None:
        pass

    def started(self):
        print("vehical started")
    
    def stop(self):
        print("vehival stop")

class Car(Vehical):
     def horn(self):
        print("honk honk")

     
mycar=Car()
mycar.started()
mycar.horn()
mycar.stop()