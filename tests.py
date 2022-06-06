import unittest
from algorithms import get_paths_size
import testfiles
import os


def types(paths_size, types_files):
    size = ["K", "M", "G"]
    for i in range(size.index(types_files) + 1):
        paths_size /= 1024
    return paths_size


class TestSizesBytes(unittest.TestCase):

    def testAll(self):
        self.assertEqual(37000000,
                         sum(get_paths_size(os.path.join
                                            (os.getcwd(),
                                             testfiles.__name__),
                                            "", "", "")[1]))

    def testTypesE(self):
        self.assertEqual(35000000,
                         sum(get_paths_size(os.path.join
                                            (os.getcwd(),
                                             testfiles.__name__),
                                            "", "e", "docx")[1]))

    def testTypesI(self):
        self.assertEqual(2000000,
                         sum(get_paths_size(os.path.join
                                            (os.getcwd(),
                                             testfiles.__name__),
                                            "", "i", "docx")[1]))


class TestCurrentSizes(unittest.TestCase):
    def testK(self):
        self.assertEqual(36132.8125,
                         types(sum(get_paths_size(os.path.join
                                                  (os.getcwd(),
                                                   testfiles.__name__),
                                                  "", "", "")[1]), "K"))

    def testM(self):
        self.assertEqual(35.28594970703125,
                         types(sum(get_paths_size(os.path.join
                                                  (os.getcwd(),
                                                   testfiles.__name__),
                                                  "", "", "")[1]), "M"))

    def testG(self):
        self.assertEqual(0.034458935260772705,
                         types(sum(get_paths_size(os.path.join
                                                  (os.getcwd(),
                                                   testfiles.__name__),
                                                  "", "", "")[1]), "G"))
