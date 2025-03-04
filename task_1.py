import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Abstract class for vehicles
class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass


# Car class inherits from Vehicle
class Car(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Engine started")
        print(f"{self.make} {self.model} ({self.region} Spec): Engine started")


# Motorcycle class inherits from Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Engine started")
        print(f"{self.make} {self.model} ({self.region} Spec): Engine started")


# Abstract factory for creating vehicles
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


# Factory for creating US vehicles
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        logging.info(f"Creating US car: {make} {model}")
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        logging.info(f"Creating US motorcycle: {make} {model}")
        return Motorcycle(make, model, "US")


# Factory for creating EU vehicles
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        logging.info(f"Creating EU car: {make} {model}")
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        logging.info(f"Creating EU motorcycle: {make} {model}")
        return Motorcycle(make, model, "EU")


# Using the factories to create vehicles
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
