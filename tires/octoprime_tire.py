from tires.tires import Tires

class OctoprimeTire(Tires):
    def __init__(self,Octoprime_sensor):
        self.range = (0, 4)
        self.Octoprime_sensor = range
        self.Octoprime_sensor_worn = sum(range) >= 3

    def needs_service(self):
        date_OctoprimeTire_needs_to_be_serviced_by = self.Octoprime_sensor_worn
        if date_OctoprimeTire_needs_to_be_serviced_by:
            return True
        else:
            return False

