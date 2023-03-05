import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_lower(self):
        self.assertEqual('HELLO'.lower(), 'hello')
