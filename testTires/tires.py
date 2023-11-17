from abc import ABC


class Tires(ABC):
    def needs_service(self, tire_wear):
        pass


class CarriganTires(Tires):
    def needs_service(self, tire_wear):
        return any(wear >= 0.9 for wear in tire_wear)


class OctoprimeTires(Tires):
    def needs_service(self, tire_wear):
        return sum(tire_wear) >= 3
