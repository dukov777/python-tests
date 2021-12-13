class Port(object):
    
    _data = 0
    _pin_value = 0

    def __init__(self) -> None:
        object.__init__(self)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
    
    def __getattr__(self, name):
        if 'pin' in name:
            return self._pin_value
        else:
            return object.__getattribute__(self, name)

    def write(self, data):
        self._data = data

    def read(self):
        return self._data


import unittest

class TestGlobalVars(unittest.TestCase):
    def setUp(self):
        self.port1 = Port()
        self.port2 = Port()

    def test_global_equals(self):
        self.assertEqual(self.port1._pin_value, self.port2._pin_value)

    def test_global_different(self):
        self.port1._pin_value = 1
        self.assertNotEqual(self.port1._pin_value, self.port2._pin_value)

    def test_global_different2(self):
        Port._pin_value = 2
        self.assertNotEqual(self.port1._pin_value, self.port2._pin_value)


class TestForUnsupportedProperties(unittest.TestCase):
    def setUp(self):
        self.port = Port()

    def test_unsupported(self):
        with self.assertRaises(AttributeError):
            self.port.randomMember

class TestDefaultPin(unittest.TestCase):
    def setUp(self):
        self.port = Port()

    def test_read_default(self):
        self.assertEqual(self.port.pin1, 0)

class TestPin(unittest.TestCase):
    def setUp(self):
        self.port = Port()

    def test_read_1(self):
        self.port.pin1 = 1
        self.assertEqual(self.port.pin1, 1)

    def test_read_0(self):
        self.port.pin1 = 0
        self.assertEqual(self.port.pin1, 0)

class TestPort(unittest.TestCase):
    def setUp(self):
        self.port = Port()

    def test_read_default(self):
        self.assertEqual(self.port.read(), 0)

    def test_read(self):
        self.port.write(10)
        self.assertEqual(self.port.read(), 10)


class Serial(object):
    def __init__(self) -> None:
        self.__dict__['_value'] = []
        super().__init__()

    def __setattr__(self, name, value):
        if name == 'spi1':
            self.__dict__['_value'] = value
    
    def __getattribute__(self, item):
        if item == 'spi1':
            return self.__dict__['_value']   
        return super().__getattribute__(item)


import unittest
class SerialSpi1Read(unittest.TestCase):
    def setUp(self):
        self.serial = Serial()

    def test_read_default(self):
        self.assertEqual(self.serial.spi1, [],
                         'incorrect default size')

    def test_read_internal_state(self):
        self.serial.__dict__['_value'] = [1, 2, 3]
        self.assertEqual(self.serial.spi1, [1,2,3], 'incorrect value')

class SerialSpi1Write(unittest.TestCase):
    def setUp(self):
        self.serial = Serial()

    def test_write(self):
        self.serial.spi1 = [1, 2, 3]
        self.assertEqual(self.serial.spi1, [1, 2, 3], 'incorrect data')


if __name__ == '__main__':
    unittest.main()
