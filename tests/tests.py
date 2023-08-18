import testfiles
from src.algorithms import get_paths_size

import os
import unittest


def types(paths_size, types_files):
    size = ["K", "M", "G"]
    for i in range(size.index(types_files) + 1):
        paths_size /= 1024
    return paths_size


class TestSizesBytes(unittest.TestCase):

    def testAll(self):
        expected = 37000000
        result = sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "", [])[1])
        self.assertEqual(expected, result)

    def testTypesE(self):
        expected = 35000000
        result = sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "e", ["docx"])[1])
        self.assertEqual(expected, result)

    def testTypesI(self):
        expected = 2000000
        result = sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "i", ["docx"])[1])
        self.assertEqual(expected, result)


class TestCurrentSizes(unittest.TestCase):
    def testK(self):
        expected = 36132.8125
        result = types(sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "", [])[1]), "K")
        self.assertEqual(expected, result)

    def testM(self):
        expected = 35.28594970703125
        result = types(sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "", [])[1]), "M")
        self.assertEqual(expected, result)

    def testG(self):
        expected = 0.034458935260772705
        result = types(sum(get_paths_size(os.path.join(os.getcwd(), testfiles.__name__), False, "", [])[1]), "G")
        self.assertEqual(expected, result)
