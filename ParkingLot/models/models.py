from datetime import datetime
from enum import Enum
from typing import List
from weakref import finalize


class Basemodel:
    def __init__(self,id:int):
        self.id=id
        self.created_at=datetime.now()
        self.updated_at=datetime.now()

class BillStatus(Enum):
    PAID='PAID'
    PENDING='PENDING'
    PARTIALLY_PAID='PARTIALLY_PAID'

class FloorStatus(Enum):
    OPEN='OPEN'
    CLOSED='CLOSED'
    FULL='FULL'
    UNDER_MAINTENANCE='UNDER_MAINTENANCE'

class GateStatus(Enum):
    OPEN='OPEN'
    CLOSED = 'CLOSED'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'

class GateType(Enum):
    ENTRY='ENTRY'
    EXIT='EXIT'

class ParkingLotStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'

class PaymentModes(Enum):
    CASH='CASH'
    ONLINE='ONLINE'
    CARD='CARD'
    UPI='UPI'

class PaymentStatus(Enum):
    SUCCESS='SUCCESS'
    FAILED='FAILED'

class SlotStatus(Enum):
    FILLED='FILLED'
    EMPTY='EMPTY'
    RESERVED='RESERVED'
    BLOCKED='BLOCKED'

class SlotAssignmentStrateyEnum(Enum):
    RANDOM='RANDOM'

class VehicleType(Enum):
    CAR = 'CAR'
    BIKE = 'BIKE'
    BUS = 'BUS'
    TRUCK = 'TRUCK'

class Bill(Basemodel):
    def __init__(self,id:int,
                 ticket:'Ticket',
                 exit_time:datetime,
                 exited_at,payments:list,
                 total_amount:int,
                 bill_status:BillStatus):
        super().__init__(id)
        self.ticket=ticket
        self.exit_time=exit_time
        self.exited_at=exited_at
        self.payments=payments
        self.total_amount=total_amount
        self.bill_status=bill_status

    def get_amount_paid(self):
        return sum(p.amount for p in self.payments if p.payment_status==PaymentStatus.SUCCESS)

    def get_amount_due(self):
        return max(0,self.total_amount-self.get_amount_paid())

    def is_fully_paid(self):
        return self.get_amount_paid()>=self.total_amount

    def __str__(self):
        return f"Bill(ID={self.id}, Amount={self.total_amount}, " \
               f"Status={self.bill_status.value}, Ticket={self.ticket.number if self.ticket else 'N/A'})"

    def __repr__(self):
        return self.__str__()
class Floor(Basemodel):
    def __init__(self,id:int,
                 parking_slot_list:list,
                 floor_number:int ,
                 floor_status:FloorStatus,
                 allowed_vehicles:list[VehicleType]):
        super().__init__(id)
        self.parking_slot_list=parking_slot_list
        self.floor_number=floor_number
        self.floor_status=floor_status
        self.allowed_vehicles=allowed_vehicles

    def __str__(self):
        return f"Floor({self.floor_number}, {self.floor_status.value})"

    def __repr__(self):
        return self.__str__()

class Gate(Basemodel):
    def __init__(self,id:int,gate_number:int,gate_type:GateType,parking_lot,gate_status:GateStatus,):
        super().__init__(id)
        self.gate_number=gate_number
        self.gate_type=gate_type
        self.parking_lot=parking_lot
        self.gate_status=gate_status

class ParkingLot(Basemodel):
    def __init__(self,id:int,name:str,address:str,parking_floors:list[Floor],gates:List[Gate],allowed_vehicles:list[VehicleType],capacity:int,status:ParkingLotStatus,slot_assignment_strategy:SlotAssignmentStrateyEnum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy

class Payment(Basemodel):
    def __init__(self,id:int,amount:int,
                 payment_mode:PaymentModes,
                 ref_id:str,bill,
                 payment_status:PaymentStatus,
                 paid_at:datetime):
        super().__init__(id)
        if amount<=0:
            raise ValueError('Payment amount must be positive')
        if not ref_id:
            raise ValueError("Reference ID is required")
        self.amount = amount
        self.payment_mode = payment_mode
        self.ref_id = ref_id
        self.bill = bill
        self.payment_status = payment_status
        self.paid_at = paid_at

    def __str__(self):
        return f"Payment(ID={self.id}, Amount={self.amount}, " \
               f"Mode={self.payment_mode.value}, Status={self.payment_status.value}, " \
               f"Ref={self.ref_id[:10]}..., Bill={self.bill.id if self.bill else 'N/A'})"

    def __repr__(self):
        return self.__str__()


class Slot(Basemodel):
    def __init__(self,id:int,slot_number:int,vehicle_type:VehicleType,parking_slot_status:SlotStatus,parking_floor:Floor):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor

    def __str__(self):
        return f"Slot({self.slot_number}, {self.vehicle_type.value}, {self.parking_slot_status.value})"

    def __repr__(self):
        return self.__str__()

class Ticket(Basemodel):
    def __init__(self,id:int,number:int,entry_time:datetime,vehicle,parking_slot:Slot,generated_gate:Gate):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_gate = generated_gate

class Vehicle(Basemodel):
    def __init__(self,id:int,vehicle_number:str,owner_name:str,vehicle_type:VehicleType):
        super().__init__(id)
        self.vehicle_number=vehicle_number
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type


















