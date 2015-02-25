#!/usr/bin/env python
from AlphaTwirl import TreeReaderPackage
import unittest

##____________________________________________________________________________||
class MockReader(object):
    pass

##____________________________________________________________________________||
class MockCollector(object):
    def __init__(self):
        self.readers = [ ]
        self.collected = False

    def addReader(self, datasetName, reader):
        self.readers.append((datasetName, reader))

    def collect(self):
        self.collected = True

##____________________________________________________________________________||
class TestTreeReaderPackage(unittest.TestCase):

    def test_make(self):
        collector = MockCollector()
        package = TreeReaderPackage(MockReader, collector)

        reader = package.make("data1")
        self.assertIsInstance(reader, MockReader)

        self.assertEqual([("data1", reader)], collector.readers)

    def test_collect(self):
        collector = MockCollector()
        package = TreeReaderPackage(MockReader, collector)

        self.assertFalse(collector.collected)
        package.collect()
        self.assertTrue(collector.collected)

##____________________________________________________________________________||
