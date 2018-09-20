from yeelight import Bulb
from yeelight import BulbType
from yeelight import discover_bulbs

class ColorBulb(Bulb):
    pass

class WhiteBulb(Bulb):
    pass


class BulbsController(object):

    def __init__(self):
        self._bulbs = []
        self._discover_bulbs()
        self.get_bulbs_type(None)
    def get_bulbs(self):
        return self._bulbs

    def _discover_bulbs(self):
        bulbs = discover_bulbs()
        self._size = len(bulbs)
        for bulb in bulbs:
            print bulb['capabilities']
            self._bulbs.append(Bulb(bulb['ip']))

    def refresh(self):
        self._discover_bulbs()

    def get_bulbs_number(self):
        return self._size

    def count_bulb_type(self, bulb_type):
        counter = 0
        for bulb in self._bulbs:
            if bulb.bulb_type == BulbType.Unknown:
                bulb.get_properties()
            if bulb.bulb_type == bulb_type:
                counter += 1
        return counter

    def get_bulbs_type(self, bulb_type):
        bulbs = []
        for bulb in self._bulbs:
            if bulb.bulb_type == BulbType.Unknown:
                bulb.get_properties()
            if bulb.bulb_type == bulb_type:
                bulbs.append(bulb)
        return bulbs

if __name__ == '__main__':
    bc = BulbsController()
    print bc.count_bulb_type(BulbType.Color)
    print bc.count_bulb_type(BulbType.WhiteTemp)
