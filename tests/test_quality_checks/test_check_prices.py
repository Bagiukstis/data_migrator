import unittest
from quality_checks.check_prices import checkprices
import pandas as pd

table_name = "sample"


class TestCheckPrices(unittest.TestCase):
    def test_no_negative_prices(self):
        data = {
            "product_name": ["Product 1", "Product 2", "Product 3"],
            "list_price": [10.99, 20.50, 15.75],
        }
        df = pd.DataFrame(data)

        result = checkprices(df, table_name)

        self.assertFalse(
            result,
            "Expected the function to return False for DataFrame with no negative prices",
        )

    def test_negative_prices_present(self):
        data = {
            "product_name": ["Product 1", "Product 2", "Product 3"],
            "list_price": [-10.99, 20.50, -5.75],
        }
        df = pd.DataFrame(data)

        result = checkprices(df, table_name)

        self.assertTrue(
            result,
            "Expected the function to return True for DataFrame with negative prices",
        )

    def test_empty_dataframe(self):
        df = pd.DataFrame()

        result = checkprices(df, table_name)

        self.assertFalse(
            result, "Expected the function to return False for an empty DataFrame"
        )
