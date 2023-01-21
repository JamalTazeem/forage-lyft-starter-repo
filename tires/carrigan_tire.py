from tires.tires import Tires

class CarriganTire(Tires):
    def __init__(self, CarriganTire_sensor):
        self.CarriganTire_sensor = range(0, 1)
        self.CarriganTire_sensor_worn = range >= 0.9

    def needs_service(self):
        date_CarriganTire_needs_to_be_serviced_by = self.CarriganTire_sensor_worn
        if date_CarriganTire_needs_to_be_serviced_by:
            return True
        else:
            return False


