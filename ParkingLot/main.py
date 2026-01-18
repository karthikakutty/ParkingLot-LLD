from ParkingLot.repo.GateRepo import GateRepo
from ParkingLot.repo.ParkingLotRepo import ParkingLotRepo
from ParkingLot.repo.VehicleRepo import VehicleRepo
from ParkingLot.repo.slotRepo import SlotRepo
from ParkingLot.repo.ticketRepo import TicketRepo
from ParkingLot.models.models import *
from ParkingLot.dtos.IssueTokenRequest import IssueTokenRequest
from ParkingLot.service.TicketService import TicketService
from ParkingLot.controller.TicketController import TicketController
from ParkingLot.dtos.TicketResponse import TicketResponse
from ParkingLot.repo.BillRepo import BillRepo
from ParkingLot.repo.PaymentRepo import PaymentRepo
from ParkingLot.service.BillService import BillService
from ParkingLot.controller.BillController import BillController
from ParkingLot.dtos.BillRequestDTO import BillRequestDTO
from datetime import datetime, timedelta


def setup_initial_date(gate_repo:GateRepo,parking_lot_repo:ParkingLotRepo,slot_repo:SlotRepo):
    #create parking lot
    parking_lot=ParkingLot(id=1,
                           name="Main Parking Lot",
                           address='23 main str',
                           parking_floors=[],
                           gates=[],
                           allowed_vehicles=[VehicleType.CAR,VehicleType.BIKE],
                           capacity=100,
                           status=ParkingLotStatus.OPEN,
                           slot_assignment_strategy=SlotAssignmentStrateyEnum.RANDOM
                           )

    #create floor
    floor=Floor(
        id=1,
        parking_slot_list=[],
        floor_number=1,
        floor_status=FloorStatus.OPEN,
        allowed_vehicles=[VehicleType.CAR,VehicleType.BIKE])
    #create slot
    slot1=Slot(
        id=1,
        slot_number=1,
        vehicle_type=VehicleType.CAR,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor )

    slot2=Slot(
        id=2,
        slot_number=2,
        vehicle_type=VehicleType.BIKE,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor )

    #Assign slots to floor
    floor.parking_slot_list=[slot1,slot2]

    #Assign Floor to ParkingLot
    parking_lot.parking_floors=[floor]

    #create Gates
    gate=Gate(
        id=1,
        gate_number=1,
        gate_type=GateType.ENTRY,
        parking_lot=parking_lot,
        gate_status=GateStatus.OPEN )

    #Assign Gates to Parkinglot
    parking_lot.gates=[gate]

    #save to repositories
    gate_repo.gate_map[gate.id]=gate
    parking_lot_repo.parkingLots[parking_lot.id]=parking_lot
    slot_repo.slots[slot1.id]=slot1
    slot_repo.slots[slot2.id]=slot2


def test_capacity_flow(ticketRepo=None, slotRepo=None, parkingLotRepo=None):
    print("\n" + "=" * 50)
    print("TESTING CAPACITY FLOW")
    print("=" * 50)

    # Setup fresh
    gate_repo = GateRepo()
    vehicleRepo = VehicleRepo()
    slotRepo = SlotRepo()
    ticketRepo = TicketRepo()
    parkingLotRepo = ParkingLotRepo()
    setup_initial_date(gate_repo, parkingLotRepo, slotRepo)

    # Initial state
    parking_lot = parkingLotRepo.parkingLots[1]
    print(f"1. Initial capacity: {parking_lot.capacity}")

    # Issue ticket
    ticketService = TicketService(gate_repo, vehicleRepo, slotRepo, parkingLotRepo, ticketRepo)
    ticketController = TicketController(ticketService)

    request = IssueTokenRequest(
        vehicleNumber='TEST-456',
        ownerName='test',
        gateId=1,
        vehicleType=VehicleType.CAR
    )

    response = ticketController.issue_ticket(request)
    print(f"2. After ticket issuance: {parking_lot.capacity}")

    # Generate bill
    bill_repo = BillRepo()
    payment_repo = PaymentRepo()
    bill_service = BillService(ticketRepo, bill_repo, payment_repo, slotRepo, parkingLotRepo)

    bill_request = BillRequestDTO(
        ticket_id=response.TicketId,
        exit_time=datetime.now() + timedelta(hours=1),
        payment_mode=None,
        amount_paid=0
    )

    bill_controller = BillController(bill_service)
    bill_response = bill_controller.generate_bill(bill_request)
    print(f"3. After bill generation: {parking_lot.capacity}")

    # Make payment
    bill_controller.make_payment(
        bill_id=bill_response.bill_id,
        amount=bill_response.total_amount,
        payment_mode=PaymentModes.CASH
    )

    print(f"4. After payment (should be back to 100): {parking_lot.capacity}")
    print("=" * 50)

if __name__=='__main__':
    gate_repo=GateRepo()
    vehicleRepo=VehicleRepo()
    slotRepo=SlotRepo()
    ticketRepo=TicketRepo()
    parkingLotRepo=ParkingLotRepo()
    setup_initial_date(gate_repo,parkingLotRepo,slotRepo)

    ticketService=TicketService(gate_repo,vehicleRepo,slotRepo,parkingLotRepo,ticketRepo)
    ticketController=TicketController(ticketService)

    request=IssueTokenRequest(
        vehicleNumber='123',
        ownerName='manish',
        gateId=1,
        vehicleType=VehicleType.CAR)

    response=ticketController.issue_ticket(request)
    print("=== Ticket Issued Successfully ===")
    print(response)


    # Optional: Print more details
    print("\n=== Detailed Information ===")
    print(f"Ticket ID: {response.TicketId}")
    print(f"Vehicle Number: {response.Vehicle}")
    print(f"Owner Name: manish")
    print(f"Vehicle Type: CAR")
    print(f"Slot Number: {response.slot.slot_number if response.slot else 'N/A'}")
    print(f"Floor Number: {response.floor.floor_number if response.floor else 'N/A'}")
    print(f"Entry Time: {response.entryTime}")
    print(f"Status: {response.Status}")

    # Check repository state
    print("\n=== Repository Status ===")
    print(f"Total tickets issued: {ticketRepo.count + 1}")
    print(f"Available slots: {len([s for s in slotRepo.slots.values() if s.parking_slot_status == SlotStatus.EMPTY])}")
    print(f"Parking lot capacity: {parkingLotRepo.parkingLots[1].capacity}")
#test the billing system
    test_capacity_flow(ticketRepo,slotRepo, parkingLotRepo)

