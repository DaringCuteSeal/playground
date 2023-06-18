from abc import ABC, abstractmethod

class LandCapable(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(LandCapable):
    def drive(self):
        print("Sedan is driving")

class Ferry():
    def ride(self):
        print("Ferry is sailing...")

class SUV(LandCapable):
    def drive(self):
        print("SUV is driving...")

def road_trip(vehicle: LandCapable):
    vehicle.drive()

a = Ferry()
road_trip(a)