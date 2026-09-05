from abc import ABC, abstractmethod

#Strategy Interface 
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, order) -> float:
        pass


#Concrete Strategies
class FlatRateShipping(ShippingStrategy):
    def calculate(self, order) -> float:
        return 10.0

class WeightBasedShipping(ShippingStrategy):
    def calculate(self, order) -> float:
        return 0.5 * order.weight

class FreeShipping(ShippingStrategy):
    def calculate(self, order) -> float:
        return 0.0

class ThirdPartyApiShipping(ShippingStrategy):
    def calculate(self, order) -> float:
        return self._call_carrier_api(order)

    def _call_carrier_api(self, order) -> float:
        return 15.0


#Context Class
class ShippingContext:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def get_cost(self, order) -> float:
        return self.strategy.calculate(order)


#Client Code
class Order:
    def __init__(self, weight: float, height: float):
        self.weight = weight
        self.height = height

order = Order(10.0, 10.0)
service = ShippingContext(FlatRateShipping())
cost = service.get_cost(order)
print(f"Cost: {cost}")

service.set_strategy(WeightBasedShipping())
cost = service.get_cost(order)
print(f"Cost: {cost}")

service.set_strategy(FreeShipping())
cost = service.get_cost(order)
print(f"Cost: {cost}")
