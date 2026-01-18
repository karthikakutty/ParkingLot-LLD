
class TicketRepo:
    def __init__(self):
        self.count=-1
        self.tickets={}

    def save_tickets(self,ticket):
        newId=self.count+1
        ticket.number=newId
        ticket.id=newId
        self.tickets[newId]=ticket
        self.count+=1
        return ticket