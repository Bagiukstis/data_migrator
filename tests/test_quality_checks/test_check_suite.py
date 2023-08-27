import unittest
from tests.test_quality_checks.test_check_na import TestCheckNa
from tests.test_quality_checks.test_check_email import TestCheckEmails
from tests.test_quality_checks.test_check_dates import TestCheckDates
from tests.test_quality_checks.test_check_dupes import TestCheckDupes
from tests.test_quality_checks.test_check_prices import TestCheckPrices


def suite():
    """Creating test suites for test_quality_checks"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCheckNa))
    test_suite.addTest(unittest.makeSuite(TestCheckEmails))
    test_suite.addTest(unittest.makeSuite(TestCheckDates))
    test_suite.addTest(unittest.makeSuite(TestCheckDupes))
    test_suite.addTest(unittest.makeSuite(TestCheckPrices))
    return test_suite
