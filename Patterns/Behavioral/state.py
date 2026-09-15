#Each state = its own class. All logic for "what happens in this state" lives inside that one state's class
# — not in a giant switch statement.
# • States decide their own transitions. A state class itself decides when to move to the next state, by
# telling the main object to switch to a new state object.

# Vending machine example

from abc import ABC, abstractmethod


# ----------- State Interface -----------
class MachineState(ABC):
    @abstractmethod
    def select_item(self, machine, item_code: str):
        pass

    @abstractmethod
    def insert_coin(self, machine, amount: int):
        pass

    @abstractmethod
    def dispense_item(self, machine):
        pass


# ----------- Concrete States -----------
class IdleState(MachineState):
    def select_item(self, machine, item_code: str):
        print(f"Item {item_code} selected")
        machine.selected_item = item_code
        machine.set_state(ItemSelectedState())

    def insert_coin(self, machine, amount: int):
        print("Select an item first before inserting coins.")

    def dispense_item(self, machine):
        print("Select an item first before dispensing.")


class ItemSelectedState(MachineState):
    def select_item(self, machine, item_code: str):
        print(f"Item {item_code} already selected")

    def insert_coin(self, machine, amount: int):
        print(f"Inserted {amount} coins")
        machine.balance += amount
        if machine.balance >= machine.item_price:
            machine.set_state(HasMoneyState())
        else:
            print(f"Insufficient balance. Please insert more coins. (Needed: {machine.item_price - machine.balance})")

    def dispense_item(self, machine):
        print("Dispensing item...")


class HasMoneyState(MachineState):
    def select_item(self, machine, item_code: str):
        print("Item already selected")

    def insert_coin(self, machine, amount: int):
        print(f"Inserted {amount} coins No more coins allowed")

    def dispense_item(self, machine):
        print("Dispensing item...")
    

# ----------- Main Machine Class -----------
class VendingMachine:
    def __init__(self, item_price: int = 1):
        self.state: MachineState = IdleState()
        self.selected_item = None
        self.balance = 0
        self.item_price = item_price

    def set_state(self, new_state: MachineState):
        self.state = new_state
        print(f"State changed to: {type(self.state).__name__}")

    def select_item(self, item_code: str):
        self.state.select_item(self, item_code)

    def insert_coin(self, amount: int):
        self.state.insert_coin(self, amount)

    def dispense_item(self):
        self.state.dispense_item(self)
    

# ----------- Client Code -----------
if __name__ == "__main__":
    machine = VendingMachine()
    machine.select_item("A1")
    machine.insert_coin(1)
    machine.dispense_item()

    
    
        