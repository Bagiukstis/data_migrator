import unittest
from quality_checks.check_email import checkemail
import pandas as pd

table_name = "sample"


class TestCheckEmails(unittest.TestCase):
    def test_valid_emails(self):
        data = {"email": ["user1@example.com", "user2@example.com"]}
        df = pd.DataFrame(data)

        result = checkemail(df, table_name)

        self.assertFalse(
            result, "Expected the function to return False for all valid emails"
        )

    def test_invalid_emails_present(self):
        data = {"email": ["user1@example.com", "invalidemail", "user3@example.com"]}
        df = pd.DataFrame(data)

        result = checkemail(df, table_name)

        self.assertTrue(
            result, "Expected the function to return True for invalid emails"
        )

    def test_empty_dataframe(self):
        df = pd.DataFrame()

        result = checkemail(df, table_name)

        self.assertFalse(
            result, "Expected the function to return False for an empty DataFrame"
        )

    def test_invalid_emails_present_2(self):
        data = {
            "email": ["userą1@example.com", "user2@ėxample.com", "user3@examplš.com"]
        }
        df = pd.DataFrame(data)

        result = checkemail(df, table_name)

        self.assertTrue(
            result, "Expected the function to return True for invalid emails"
        )
