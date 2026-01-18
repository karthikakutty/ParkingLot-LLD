class PricingFactory:
    @staticmethod
    def get_pricing_strategy(strategy_type: str = "HOURLY"):
        if strategy_type == "HOURLY":
            from ParkingLot.strgy.pricing_strategy import HourlyPricingStrategy
            return HourlyPricingStrategy()
        elif strategy_type == "FIXED_PLUS_HOURLY":
            from ParkingLot.strgy.pricing_strategy import FixedPlusHourlyPricingStrategy
            return FixedPlusHourlyPricingStrategy()
        else:
            raise ValueError(f"Unknown pricing strategy: {strategy_type}")