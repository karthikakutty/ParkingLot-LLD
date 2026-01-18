from ParkingLot.models.models import *
from ParkingLot.strgy.pricing_factory import PricingFactory
from ParkingLot.dtos.BillRequestDTO import BillRequestDTO

class BillService:
    def __init__(self, ticket_repo, bill_repo, payment_repo, slot_repo,
                 parking_lot_repo, pricing_strategy_type="HOURLY"):
        self.ticket_repo = ticket_repo
        self.bill_repo = bill_repo
        self.payment_repo = payment_repo
        self.slot_repo = slot_repo
        self.parking_lot_repo = parking_lot_repo
        self.pricing_strategy = PricingFactory.get_pricing_strategy(pricing_strategy_type)

    def generate_bill(self, request: BillRequestDTO) -> Bill:
        """Generate a bill for a ticket"""
        # Find the ticket
        ticket = self.ticket_repo.tickets.get(request.ticket_id)
        if not ticket:
            raise Exception(f"Ticket not found with ID: {request.ticket_id}")

        # Check if bill already exists
        existing_bill = self.bill_repo.find_bill_by_ticket_id(request.ticket_id)
        if existing_bill:
            raise Exception(f"Bill already exists for ticket ID: {request.ticket_id}")

            # Calculate amount
        amount = self.pricing_strategy.calculate_amount(
            ticket.entry_time,
            request.exit_time,
            ticket.vehicle.vehicle_type
        )

        # Create bill
        bill = Bill(
            id=-1,
            ticket=ticket,
            exit_time=request.exit_time,
            exited_at=request.exit_time,  # Same as exit_time
            payments=[],  # Start with empty payments list
            total_amount=amount,
            bill_status=BillStatus.PENDING
        )

        # Save bill
        saved_bill = self.bill_repo.save_bill(bill)

        # If partial payment provided, process it
        if request.amount_paid > 0 and request.payment_mode:
            self._process_payment(saved_bill, request.amount_paid, request.payment_mode)

        return saved_bill


    def _process_payment(self, bill: Bill, amount: int, payment_mode: PaymentModes) -> Payment:
        """Process a payment for a bill"""
        # Create payment
        payment = Payment(
            id=-1,
            amount=amount,
            payment_mode=payment_mode,
            ref_id=f"PAY-{bill.id}-{datetime.now().timestamp()}",
            bill=bill,
            payment_status=PaymentStatus.SUCCESS,
            paid_at=datetime.now()
        )

        # Save payment
        saved_payment = self.payment_repo.save_payment(payment)

        # Add payment to bill's payments list
        bill.payments.append(saved_payment)

        # Calculate total paid from bill's payments
        total_paid = sum(p.amount for p in bill.payments if p.payment_status == PaymentStatus.SUCCESS)

        # Update bill status
        if total_paid >= bill.total_amount:
            bill.bill_status = BillStatus.PAID
            self._free_up_resources(bill.ticket)
        elif total_paid > 0:
            bill.bill_status = BillStatus.PARTIALLY_PAID
        else:
            bill.bill_status = BillStatus.PENDING

        # Update bill in repository
        self.bill_repo.update_bill(bill)

        return saved_payment

    def _free_up_resources(self, ticket: Ticket):
        """Free up parking slot and update capacity when bill is paid"""
        # Update slot status to EMPTY
        if ticket.parking_slot:
            self.slot_repo.update_slot_status(ticket.parking_slot, SlotStatus.EMPTY)

        # Update parking lot capacity
        if ticket.generated_gate and ticket.generated_gate.parking_lot:
            parking_lot = ticket.generated_gate.parking_lot
            self.parking_lot_repo.update_parking_lot_count(parking_lot, increment=True)
    def make_payment(self, bill_id: int, amount: int, payment_mode: PaymentModes) -> Payment:
        """Make a payment towards a bill"""
        bill = self.bill_repo.find_bill_by_id(bill_id)
        if not bill:
            raise Exception(f"Bill not found with ID: {bill_id}")

        if bill.bill_status == BillStatus.PAID:
            raise Exception("Bill is already paid in full")

        return self._process_payment(bill, amount, payment_mode)

    def get_bill_details(self, bill_id: int) -> Bill:
        """Get detailed bill information"""
        bill = self.bill_repo.find_bill_by_id(bill_id)
        if not bill:
            raise Exception(f"Bill not found with ID: {bill_id}")

        return bill

    def get_bill_by_ticket(self, ticket_id: int) -> Bill:
        """Get bill by ticket ID"""
        bill = self.bill_repo.find_bill_by_ticket_id(ticket_id)
        if not bill:
            raise Exception(f"No bill found for ticket ID: {ticket_id}")

        return bill