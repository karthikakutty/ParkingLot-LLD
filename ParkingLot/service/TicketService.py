from datetime import datetime
from ParkingLot.models.models import *
from ParkingLot.strgy.getSlotFactory import Slotfactory
from ParkingLot.strgy import *

class TicketService:
    def __init__(self,gateRepo, vehicleRepo, slotRepo, parkingLotRepo, ticketRepo):
        self.gateRepo =gateRepo
        self.vehicleRepo = vehicleRepo
        self.slotRepo = slotRepo
        self.parkingLotRepo = parkingLotRepo
        self.ticketRepo = ticketRepo

    def issueTicket(self,vehicle_number,owner_name,gate_id,vehicleType)->Ticket:

        #create ticket
        ticket=Ticket(id=-1, number="",
                      entry_time=datetime.now(),
                      vehicle=None,
                      parking_slot=None,
                      generated_gate=None)

        #set info...like gate no...
        gate=self.gateRepo.find_gate_by_id(gate_id)
        if gate is None:
            raise Exception ("Gate not found")
        ticket.generated_gate=gate

        #vehicle info...
        vehicle=self.vehicleRepo.find_vehicle_by_number(vehicle_number)
        if vehicle is None:
            vehicle = Vehicle(id=vehicle_number,vehicle_number=vehicle_number,owner_name=owner_name,vehicle_type=vehicleType)
            self.vehicleRepo.save_vehicle(vehicle)

        ticket.vehicle=vehicle

        #find a slot
        slotStgy=Slotfactory.get_slot_stgy_obj(gate.parking_lot.slot_assignment_strategy)
        if not slotStgy:
            raise Exception ("Slot not found")
        slot=slotStgy.get_slot(vehicleType,gate)
        if not slot:
            raise Exception(f"No available slot found for vehicle type: {vehicleType}")

        ticket.parking_slot=slot

        #update slot...
        self.slotRepo.update_slot_status(slot,SlotStatus.FILLED)

        #update parking counters
        self.parkingLotRepo.update_parking_lot_count(gate.parking_lot,increment=False)

        #return ticket...
        return self.ticketRepo.save_tickets(ticket)
