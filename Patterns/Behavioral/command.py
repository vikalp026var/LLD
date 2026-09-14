from abc import ABC, abstractmethod

#Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

#Receiver class
class Light:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def on(self):
        self.is_on = True
        print(f"{self.name} light is on")

    def off(self):
        self.is_on = False
        print(f"{self.name} light is off")


class Thermostat:
    def __init__(self):
        self.temperature = 70 

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Thermostat is set to {temperature} degrees")


#Concrete Command classes

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class ThermostatSetCommand(Command):
    def __init__(self, thermostat, temperature):
        self.thermostat = thermostat
        self.temperature = temperature

    def execute(self):
        self.thermostat.set_temperature(self.temperature)

    def undo(self):
        self.thermostat.set_temperature(self.previous_temperature)

#Invoker class
class RemoteControl:
    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()

#Client code
if __name__ == "__main__":
    light = Light("Living Room")
    thermostat = Thermostat()
    remote = RemoteControl()

    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    thermostat_set_command = ThermostatSetCommand(thermostat, 75)

