from abc import ABC,abstractmethod
from datetime import datetime,timedelta
from ParkingLot.models.models import VehicleType

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_amount(self,entry_time:datetime,
                         exit_time:datetime,
                         vehicle_type:VehicleType):
        pass

class HourlyPricingStrategy(PricingStrategy):
    def __init__(self):
        # Define hourly rates for different vehicle types
        self.rates = {
            VehicleType.BIKE: 20,      # 20 per hour
            VehicleType.CAR: 50,       # 50 per hour
            VehicleType.TRUCK: 100,    # 100 per hour
            VehicleType.BUS: 150,      # 150 per hour
        }

    def calculate_amount(self,entry_time:datetime,
                         exit_time:datetime,
                         vehicle_type:VehicleType):
        duration=exit_time-entry_time
        hours=max(1,duration.total_seconds()/3600)
        rate=self.rates.get(vehicle_type,50)
        return int(hours*rate)

    class FixedPlusHourlyPricingStrategy(PricingStrategy):
        def __init__(self):
            self.fixed_rates = {
                VehicleType.BIKE: 10,
                VehicleType.CAR: 30,
                VehicleType.TRUCK: 60,
                VehicleType.BUS: 100,
            }
            self.hourly_rates = {
                VehicleType.BIKE: 15,
                VehicleType.CAR: 40,
                VehicleType.TRUCK: 80,
                VehicleType.BUS: 120,
            }

        def calculate_amount(self,entry_time:datetime,
                         exit_time:datetime,
                         vehicle_type:VehicleType):
            duration=exit_time-entry_time
            hours=max(1,duration.total_seconds()/3600)
            fixed=self.fixed_rates.get(vehicle_type,30)
            hourly=self.hourly_rates.get(vehicle_type,40)
            return int(fixed+(hours*hourly))