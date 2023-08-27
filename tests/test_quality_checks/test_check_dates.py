import unittest
from quality_checks.check_dates import checkdates
import pandas as pd

table_name = "sample"


class TestCheckDates(unittest.TestCase):
    def test_check_cols(self):
        df = pd.DataFrame({"sample_col": [1, 2, 3], "sample_col2": [4, 5, 6]})
        result = checkdates(df, table_name)
        self.assertFalse(
            result,
            'Expected False when there are no data columns ["order_date", "required_date", "shipped_date"] in the dataframe',
        )

    def test_correct_dates(self):
        df = pd.DataFrame(
            {
                "order_date": ["2023-01-01", "2023-02-01"],
                "required_date": ["2023-02-01", "2023-03-01"],
                "shipped_date": ["2023-01-15", "2023-02-20"],
            }
        )
        result = checkdates(df, table_name)
        self.assertFalse(result, "Expected False when dates are correctly formated")

    def test_wrong_dates(self):
        df = pd.DataFrame(
            {
                "order_date": ["2023-02-01", "2023-03-01"],
                "required_date": ["2023-01-01", "2023-03-15"],
                "shipped_date": ["2023-01-15", "2023-03-20"],
            }
        )
        result = checkdates(df, table_name)
        self.assertTrue(result, "Expected True when dates are wrongly formatted")


if __name__ == "__main__":
    unittest.main()
