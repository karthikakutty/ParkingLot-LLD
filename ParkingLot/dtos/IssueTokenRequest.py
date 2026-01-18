class IssueTokenRequest:
    def __init__(self,vehicleNumber,ownerName,gateId, vehicleType):
        self.vehicleNumber = vehicleNumber
        self.ownerName = ownerName
        self.gateId = gateId
        self.vehicleType = vehicleType