from ParkingLot.dtos.BillRequestDTO import BillRequestDTO
from ParkingLot.dtos.BillResponse  import BillResponseDTO
from ParkingLot.service.BillService import BillService
from ParkingLot.models.models import PaymentModes


class BillController:
    def __init__(self, bill_service: BillService):
        self.bill_service = bill_service

    def generate_bill(self, request: BillRequestDTO) -> BillResponseDTO:
        """Generate a bill for parking exit"""
        try:
            bill = self.bill_service.generate_bill(request)
            return self._convert_to_response_dto(bill)
        except Exception as e:
            response = BillResponseDTO()
            response.bill_status = "ERROR"
            print(f"Error generating bill: {e}")
            return response

    def make_payment(self, bill_id: int, amount: int,
                     payment_mode: PaymentModes = PaymentModes.CASH) -> BillResponseDTO:
        """Make payment towards a bill"""
        try:
            payment = self.bill_service.make_payment(bill_id, amount, payment_mode)
            bill = self.bill_service.get_bill_details(bill_id)
            return self._convert_to_response_dto(bill)
        except Exception as e:
            response = BillResponseDTO()
            response.bill_status = "ERROR"
            print(f"Error processing payment: {e}")
            return response

    def get_bill_details(self, bill_id: int) -> BillResponseDTO:
        """Get bill details"""
        try:
            bill = self.bill_service.get_bill_details(bill_id)
            return self._convert_to_response_dto(bill)
        except Exception as e:
            response = BillResponseDTO()
            response.bill_status = "ERROR"
            print(f"Error fetching bill details: {e}")
            return response


    def get_bill_by_ticket(self, ticket_id: int) -> BillResponseDTO:
        """Get bill by ticket ID"""
        try:
            bill = self.bill_service.get_bill_by_ticket(ticket_id)
            return self._convert_to_response_dto(bill)
        except Exception as e:
            response = BillResponseDTO()
            response.bill_status = "ERROR"
            print(f"Error fetching bill by ticket: {e}")
            return response

    def _convert_to_response_dto(self, bill) -> BillResponseDTO:
        """Convert Bill model to BillResponseDTO"""
        response = BillResponseDTO()
        response.bill_id = bill.id
        response.ticket_id = bill.ticket.id if bill.ticket else None
        response.vehicle_number = bill.ticket.vehicle.vehicle_number if bill.ticket and bill.ticket.vehicle else None
        response.entry_time = bill.ticket.entry_time if bill.ticket else None
        response.exit_time = bill.exit_time
        response.total_amount = bill.total_amount
        response.bill_status = bill.bill_status.value

        # Calculate payments from bill's payments list
        response.amount_paid = sum(p.amount for p in bill.payments if p.payment_status.value == "SUCCESS")
        response.amount_due = max(0, bill.total_amount - response.amount_paid)
        response.payments = bill.payments

        return response