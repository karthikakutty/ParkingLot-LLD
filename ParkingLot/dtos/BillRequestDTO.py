from datetime import datetime
from ParkingLot.models.models import PaymentModes

class BillRequestDTO:
    def __init__(self,ticket_id,exit_time:datetime=None,
                 payment_mode:PaymentModes=None,
                 amount_paid:int=0):
        self.ticket_id=ticket_id
        self.exit_time=exit_time
        self.payment_mode=payment_mode
        self.amount_paid=amount_paid

    def __str__(self):
        return f"BillRequest(Ticket={self.ticket_id}, ExitTime={self.exit_time}, " \
               f"PaymentMode={self.payment_mode.value if self.payment_mode else 'None'}, " \
               f"AmountPaid={self.amount_paid})"