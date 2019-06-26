from unittest import TestCase

import task5


class TestTask5(TestCase):

    def setUp(self):
        """Init"""

    def test_gorobotgo(self):
        self.assertFalse(task5.gorobotgo("ld"))
        self.assertTrue(task5.gorobotgo("lrud"))
        self.assertTrue(task5.gorobotgo(""))
        self.assertFalse(task5.gorobotgo("kjasdf kjas; dlkfj "))

    def tearDown(self):
        """Finish"""
