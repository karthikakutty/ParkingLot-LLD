from ParkingLot.models.models import Payment


class PaymentRepo:
    def __init__(self):
        self.payments={}
        self.count=0

    def save_payment(self,payment:Payment):
        if payment.id is None or payment.id==-1:
            payment.id=self.count
            self.count+=1

        self.payments[payment.id]=payment
        return payment

    def find_payments_by_bill_id(self,bill_id):
        return [p for p in self.payments.values() if p.bill and p.bill.id==bill_id]