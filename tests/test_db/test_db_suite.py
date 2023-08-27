import unittest
from tests.test_db.test_read import TestDatabaseRead
from tests.test_db.test_write import TestDatabaseWrite
from tests.test_db.test_connector import TestDatabaseConnctor


def suite():
    """Creating test suites for test_db"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestDatabaseRead))
    test_suite.addTest(unittest.makeSuite(TestDatabaseWrite))
    test_suite.addTest(unittest.makeSuite(TestDatabaseConnctor))
    return test_suite
