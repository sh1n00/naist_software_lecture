import unittest
import sys
sys.path.append("./")
from csv_reader import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))


    def test_read_value(self):
        correct = [
            ['value1A', 'value1B', 'value1C'],
            ['value2A', 'value2B', 'value2C'],
            ['value3A', 'value3B', 'value3C']]
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(correct, l)
    def test_file(self):
        with self.assertRaises(FileNotFoundError):
            CSVPrinter("sample1.csv").read()