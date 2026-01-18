from abc import ABC,abstractmethod
from ParkingLot.models.models import VehicleType,Slot,Gate

class SlotStgy(ABC):
    @abstractmethod
    def get_slot(self,vehicleType:VehicleType,gate:Gate)->Slot:
        pass