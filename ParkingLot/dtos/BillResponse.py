from ParkingLot.models.models import BillStatus


class BillResponseDTO:
    def __init__(self):
        self.bill_id = None
        self.ticket_id = None
        self.vehicle_number = None
        self.entry_time = None
        self.exit_time = None
        self.total_amount = None
        self.amount_paid = None
        self.amount_due = None
        self.bill_status = None
        self.payments = []

    def __str__(self):
        return f"BillResponse(ID={self.bill_id}, Ticket={self.ticket_id}, " \
               f"Amount={self.total_amount}, Paid={self.amount_paid}, " \
               f"Due={self.amount_due}, Status={self.bill_status})"

    def __repr__(self):
        return self.__str__()