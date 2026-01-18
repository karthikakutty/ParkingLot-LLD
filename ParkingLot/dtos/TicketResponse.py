class TicketResponse:

    def __init__(self):
        self.TicketId = None
        self.entryTime = None
        self.slot = None
        self.Status = None
        self.floor = None
        self.Vehicle = None

    def __str__(self):
        return f"TicketResponse(TicketId={self.TicketId}, " \
               f"Vehicle={self.Vehicle}, " \
               f"Status={self.Status}, " \
               f"Slot={self.slot.slot_number if self.slot else 'N/A'}, " \
               f"Floor={self.floor.floor_number if self.floor else 'N/A'}, " \
               f"EntryTime={self.entryTime})"

    def __repr__(self):
        return self.__str__()