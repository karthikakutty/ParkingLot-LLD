from ParkingLot.models.models import VehicleType, Slot,Gate,SlotStatus
from ParkingLot.strgy.slotStgy import SlotStgy


class RandomSlotFindingStgy(SlotStgy):
    def get_slot(self,vehicleType:VehicleType,gate:Gate) ->Slot:
        for floor in gate.parking_lot.parking_floors:
            if vehicleType in floor.allowed_vehicles:
                for slot in floor.parking_slot_list:
                    if slot.vehicle_type==vehicleType and slot.parking_slot_status==SlotStatus.EMPTY:
                        return slot
        return None