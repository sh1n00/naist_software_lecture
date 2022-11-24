import unittest
import sys

import csv

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines


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