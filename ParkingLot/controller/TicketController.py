from ParkingLot.dtos.IssueTokenRequest import IssueTokenRequest
from ParkingLot.dtos.TicketResponse import TicketResponse
from ParkingLot.service.TicketService import TicketService

class TicketController:
    def __init__(self,ticketService:TicketService):
        self.ticketService=ticketService

    def issue_ticket(self, request: IssueTokenRequest) -> TicketResponse:
        ticket=self.ticketService.issueTicket(request.vehicleNumber,request.ownerName,request.gateId,request.vehicleType)
        response=TicketResponse()
        response.TicketId=ticket.number
        response.slot=ticket.parking_slot
        response.Vehicle=ticket.vehicle.id
        response.entryTime=ticket.entry_time
        response.Status="SUCCESS"
        response.floor=ticket.parking_slot.parking_floor
        return response


