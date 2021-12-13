
class InstanceContainer(object):
    
    __instance_list = []

    @classmethod
    def _add_instance(cls, instance):
        cls.__instance_list.append(instance)
    
    @classmethod
    def get_instances(cls):
        return InstanceContainer.__instance_list


class InstanceX(InstanceContainer):
    def __init__(self) -> None:
        super().__init__()
        InstanceContainer._add_instance(self)


import unittest

class TestInstance(unittest.TestCase):
    def setUp(self):
        self.instance1 = InstanceX()
        self.instance2 = InstanceX()
        
    def test_created_2_instances(self):
        self.assertIn(self.instance1, InstanceContainer.get_instances())
        self.assertIn(self.instance2, InstanceContainer.get_instances())


if __name__ == '__main__':
    unittest.main()
