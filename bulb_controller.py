from yeelight import Bulb
from yeelight import BulbType
from yeelight import discover_bulbs
from yeelight import BulbException
from utils import DEFAULT_FILE_PATH,FILENAME

import os


class ColorBulb(Bulb):
    pass

class WhiteBulb(Bulb):
    pass


class BulbsController(object):

    def __init__(self):
        self._discover_bulbs()
        self._load_state_to_bulb()

    def get_bulbs(self):
        return self._bulbs

    def _discover_bulbs(self):
        self._bulbs = []
        try:
            bulbs = discover_bulbs()
        except IOError as e:
            print e
            return
        for bulb in bulbs:
            print bulb['capabilities']
            self._bulbs.append(Bulb(bulb['ip']))
        if len(self._bulbs) > 0:
            file = os.path.join(DEFAULT_FILE_PATH, FILENAME)
            self.save_bulbs_to_file(file)
        if len(self._bulbs) == 0:
            print 'discovery failed, loading from file'
            self.load_bulbs_from_file()

    def refresh(self):
        self._discover_bulbs()

    def get_bulbs_number(self):
        return len(self._bulbs)

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
                self._load_state_to_bulb(bulb)
            if bulb.bulb_type == bulb_type:
                bulbs.append(bulb)
        return bulbs

    def load_bulbs_from_file(self, file_path=os.path.join(DEFAULT_FILE_PATH, FILENAME)):
        file = open(file_path, 'r')
        self._bulbs = []
        for line in file.readlines():
            bulb = Bulb(line)
            self._bulbs.append(bulb)
        file.close()

    def _is_bulb_responding(self, bulb):
         pass#todo

    def save_bulbs_to_file(self, file_path):
        file = open(file_path, 'w')
        lines = []
        for bulb in self._bulbs:
            lines.append(bulb._ip + '\n')
        file.writelines(lines)
        file.close()

    def _load_state_to_bulb(self, bulb=None):
        if not bulb:
            for bulb in self._bulbs:
                try:
                    bulb.get_properties()
                except BulbException as e:
                    print e
        else:
            bulb.get_properties()

    def _execute_command_on_bulb(self, bulb, cmd):
            command = getattr(bulb, cmd)
            command()


if __name__ == '__main__':
    bc = BulbsController()
    print bc.count_bulb_type(BulbType.Color)
    print bc.count_bulb_type(BulbType.WhiteTemp)
    bc.load_bulbs_from_file()
