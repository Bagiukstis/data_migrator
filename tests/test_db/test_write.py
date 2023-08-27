import unittest
from unittest.mock import Mock
from sqlalchemy import create_engine
from tests.test_db._panel import Base
import pandas as pd
from db.write import Write
import os

current_file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(os.path.dirname(current_file_path))
relative_file_path = os.path.join(project_directory, "test_db/test_creds.yaml")
table_name = "sample"


class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        # Creating a mock engine
        self.mock_db_engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.mock_db_engine)

        self.db_connector = Write(relative_file_path, "MOCK_CREDS")
        self.db_connector.db = self.mock_db_engine

    def tearDown(self):
        Base.metadata.drop_all(self.mock_db_engine)

    def test_insert_data(self):
        data = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "fruits": ["Orange", "Banana", "Apple"],
                "discount": ["Yes", "No", "Yes"],
            }
        )

        result = self.db_connector.insert_data(table_name, data)
        self.assertTrue(result, "Expected True if the dataframe is inserted correctly")

    def test_insert_data_not_good(self):
        data = [1, 2, 3]
        result = self.db_connector.insert_data(table_name, data)
        self.assertFalse(result, "Expected False as the input data is not a dataframe")

    def test_insert_empty(self):
        data = pd.DataFrame()
        result = self.db_connector.insert_data(table_name, data)
        self.assertFalse(result, "Expected False as the dataframe is empty")

    def test_insert_missing_vals(self):
        data = pd.DataFrame(
            {
                "id": [1, None, 3],
                "fruits": ["Orange", "Banana", "Apple"],
                "discount": ["Yes", None, "Yes"],
            }
        )
        result = self.db_connector.insert_data(table_name, data)
        self.assertTrue(result, "Expected True if the dataframe is inserted correctly")
