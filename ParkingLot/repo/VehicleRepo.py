from ParkingLot.models.models import Vehicle

class VehicleRepo:
    def __init__(self):
        self.vehicleMap={}

    def find_vehicle_by_number(self,number):
        if number in self.vehicleMap:
            return self.vehicleMap[number]
        return None

    def save_vehicle(self,vehicle:Vehicle):
        self.vehicleMap[vehicle.vehicle_number]=vehicle
        return vehicle