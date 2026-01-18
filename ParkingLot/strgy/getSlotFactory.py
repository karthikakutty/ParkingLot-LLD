from ParkingLot.strgy.RandomSlotFindingStgy import RandomSlotFindingStgy
from ParkingLot.models.models import SlotAssignmentStrateyEnum

class Slotfactory:

    @staticmethod
    def get_slot_stgy_obj(slotStrgyEnum):
        if slotStrgyEnum==SlotAssignmentStrateyEnum.RANDOM:
            return RandomSlotFindingStgy()
        raise ValueError(f"Unknow slot strategy:{slotStrgyEnum}")
