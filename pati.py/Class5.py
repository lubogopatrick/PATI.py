class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"Drove {miles} miles. Total mileage: {self.mileage}")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")


# Usage
vehicle = Vehicle("Toyota", "Camry", 2022)
vehicle.display_info()
vehicle.drive(100)
vehicle.display_info()