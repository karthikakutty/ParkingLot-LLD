from ParkingLot.models.models import ParkingLot

class ParkingLotRepo:
    def __init__(self):
        self.parkingLots={}

    def update_parking_lot_count(self,parking_lot:ParkingLot,increment:bool=False):
        if increment:
            parking_lot.capacity +=1
        else:
            parking_lot.capacity-=1
        self.parkingLots[parking_lot.id]=parking_lot
        return parking_lot