import unittest
from tests.test_db.test_db_suite import suite as db_suite
from tests.test_quality_checks.test_check_suite import suite as quality_check_suite
import logging
import time

logging = logging.getLogger(__name__)


def master_suite():
    """Creating a master suite"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(db_suite())
    test_suite.addTest(quality_check_suite())
    return test_suite


def run_suite():
    """Running master suite"""
    logging.info("Unit testing report")
    start_time = time.time()
    runner = unittest.TextTestRunner()
    test_suite = master_suite()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        test_summary = (
            f"OK: Ran {result.testsRun} tests in {time.time() - start_time:.3f}s"
        )
    else:
        test_summary = f"FAILED: Ran {result.testsRun} tests in {time.time() - start_time:.3f}s, check console for more information"
    logging.critical(test_summary)
