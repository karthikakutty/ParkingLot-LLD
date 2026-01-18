class SlotRepo:
    def __init__(self):
        self.slots={}

    def update_slot_status(self,slot,status):
        slot.parking_slot_status=status
        self.slots[slot.id]=slot
        return slot