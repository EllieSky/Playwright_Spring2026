# 1. Custom Exceptions
class FuelDepletedError(Exception):
    """Raised when a ship does not have enough fuel for a trip."""
    pass


class HullIntegrityError(Exception):
    """Raised when a freighter exceeds its cargo limit."""
    pass


# 2. The Component Catalog (Composition)
class Engine:
    def __init__(self, model_name, fuel_efficiency, max_capacity):
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency  # Liters per Light Year
        self.max_capacity = max_capacity

    def calculate_fuel(self, distance):
        return distance * self.fuel_efficiency


# 3. The Fleet (Base Class)
class SpaceShip:
    def __init__(self, name: str, engine: Engine):
        self.name = name
        self.engine = engine  # Composition: Ship HAS-A Engine
        self.fuel_level = 2000
        self.cargo_list = []

    def refuel(self):
        self.fuel_level = self.engine.max_capacity
        print(f"--- {self.name} refueled to {self.fuel_level}L ---")

    def add_cargo(self, item):
        self.cargo_list.append(item)
        print(f"{self.name} loaded: {item}")

    def travel(self, distance):
        needed = self.engine.calculate_fuel(distance)
        if self.fuel_level < needed:
            raise FuelDepletedError(f"{self.name} needs {needed}L but only has {self.fuel_level}L.")

        self.fuel_level -= needed
        print(f"{self.name} traveled {distance}LY. Fuel remaining: {self.fuel_level}L")


# 4. Subclasses (Overriding)
class CargoFreighter(SpaceShip):
    def add_cargo(self, item):
        if len(self.cargo_list) >= 5:
            raise HullIntegrityError(f"System Alert: Cannot add {item}. Hull at max capacity!")
        super().add_cargo(item)


class ScoutShip(SpaceShip):
    def travel(self, distance):
        # Scouts are agile: 20% less fuel
        needed = self.engine.calculate_fuel(distance) * 0.8

        if self.fuel_level < needed:
            raise FuelDepletedError(f"Scout Alert: Insufficient fuel for {distance}LY jump.")

        self.fuel_level -= needed
        print(f"{self.name} (Scout) performed an agile jump of {distance}LY. Fuel: {self.fuel_level}L")


# --- 5. The Mission (Test Flow) ---

# Setup
high_perf = Engine("Hyper-Drive V12", 0.5, 5000)
budget = Engine("Rusty-Bucket 100", 2.5, 1000)

whale = CargoFreighter("The Great Whale", budget)
arrow = ScoutShip("The Silver Arrow", high_perf)

print("\n--- TEST CASE A: THE OVERLOAD ---")
try:
    for i in range(1, 7):
        whale.add_cargo(f"Crate #{i}")
except HullIntegrityError as e:
    print(e)

print("\n--- TEST CASE B: THE LONG HAUL ---")
destination_distance = 6000
try:
    arrow.travel(destination_distance)
except FuelDepletedError:
    print(f"Alert: {arrow.name} stranded! Initiating emergency refuel...")
    arrow.refuel()
    # Retry after refueling
    arrow.travel(destination_distance)
