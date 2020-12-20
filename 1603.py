class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        Keep a small array of fixed length with the number
        of slots available for each size.
        """
        self._slots = [big, medium, small]

    
    def addCar(self, carType):
        """
        Add a car to the parking lot. Return
        the add attempt if it was successful.
        """
        if self._slots[carType - 1] > 0:
            self._slots[carType - 1] -= 1
            return True
        return False
