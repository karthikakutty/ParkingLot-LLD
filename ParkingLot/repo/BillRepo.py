from ParkingLot.models.models import Bill

class BillRepo:
    def __init__(self):
        self.bills={}
        self.count=0

    def save_bill(self,bill:Bill):
        if bill.id is None or bill.id==-1:
            bill.id=self.count
            self.count+=1
        self.bills[bill.id]=bill
        return bill

    def find_bill_by_id(self,bill_id):
        return self.bills.get(bill_id)

    def find_bill_by_ticket_id(self,ticket_id):
        for bill in self.bills.values():
            if bill.ticket and bill.ticket.id==ticket_id:
                return bill
        return None

    def update_bill(self,bill:Bill):
        if bill.id in self.bills:
            self.bills[bill.id]=bill
        return bill

    def get_all_bills(self):
        return list(self.bills.values())

