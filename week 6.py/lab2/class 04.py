class Device:
    def turn_om(self):
        pass

class TV (Device):
    def turn_om(self):
        return "tv is now on"
    
class Fan (Device):
    def turn_om(self):
        return "fan is spinning now"
    
class Light(Device):
    def turn_om(self):
        return "light is on now"
    
#functionn that uses polymorphisim

def activate_device(device):
     print(device.turn_om())

tv=TV()
fan=Fan()
light=Light()


activate_device(tv)
activate_device(fan)
activate_device(light)