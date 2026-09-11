from abc import ABC, abstractmethod


# Observer interface
class FitnessDataObserver(ABC):
    @abstractmethod
    def update(self, subject: "FitnessData"):
        pass


# Subject interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Concrete Subject
class FitnessData(Subject):
    def __init__(self):
        self.observers = []
        self._steps = 0
        self._distance = 0
        self._active_minutes = 0

    def register_observer(self, observer: FitnessDataObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: FitnessDataObserver):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_steps(self, steps):
        self._steps = steps
        self.notify_observers()

    def get_steps(self):
        return self._steps

    def get_distance(self):
        return self._distance

    def get_active_minutes(self):
        return self._active_minutes


# Concrete Observer
class LiveActivityDisplay(FitnessDataObserver):
    def update(self, subject: FitnessData):
        print(f"Live Activity Display: Steps: {subject.get_steps()}, Distance: {subject.get_distance()}, Active Minutes: {subject.get_active_minutes()}")

# Concrete Observer
class WeeklySummary(FitnessDataObserver):
    def update(self, subject: FitnessData):
        print(f"Weekly Summary: Steps: {subject.get_steps()}, Distance: {subject.get_distance()}, Active Minutes: {subject.get_active_minutes()}")

# Concrete Observer
class DailySummary(FitnessDataObserver):
    def update(self, subject: FitnessData):
        print(f"Daily Summary: Steps: {subject.get_steps()}, Distance: {subject.get_distance()}, Active Minutes: {subject.get_active_minutes()}")


if __name__ == "__main__":
    fitness_data = FitnessData()
    live_activity_display = LiveActivityDisplay()
    weekly_summary = WeeklySummary()
    daily_summary = DailySummary()

    fitness_data.register_observer(live_activity_display)
    fitness_data.register_observer(weekly_summary)
    fitness_data.register_observer(daily_summary)

    fitness_data.set_steps(1000)