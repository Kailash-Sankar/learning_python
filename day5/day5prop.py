# @property is used to mask set and get methods
class Celsius(object):
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # this method gets executed when the attribute temperature accessed
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    # part of @property, the setter for the attribute
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


c = Celsius(40)
print c.temperature
print c.to_fahrenheit()
c.temperature = 37
print c.to_fahrenheit()
