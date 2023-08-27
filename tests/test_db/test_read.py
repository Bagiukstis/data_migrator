import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from db.read import Read
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tests.test_db._panel import Base, Panel
import os

current_file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(os.path.dirname(current_file_path))
relative_file_path = os.path.join(project_directory, "test_db/test_creds.yaml")

table_name = "sample"


class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        # Creating a mock engine and adding sample data
        self.mock_db_engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.mock_db_engine)
        Session = sessionmaker(bind=self.mock_db_engine)
        self.session = Session()
        self.session.add(Panel(1, "Oranges", "Yes"))
        self.session.commit()

        self.db_connector = Read(relative_file_path, "MOCK_CREDS")
        self.db_connector.db = self.mock_db_engine

    def tearDown(self):
        Base.metadata.drop_all(self.mock_db_engine)

    def test_query_compare_df_eq(self):
        result = self.db_connector.get_data(table_name)
        expected = pd.DataFrame(
            [[1, 1, "Oranges", "Yes"]], columns=["id", "category", "name", "discount"]
        )
        assert_frame_equal(result, expected)

    def test_query_nonexistent_table(self):
        table_name = "error"
        result = self.db_connector.get_data(table_name)
        self.assertEqual(
            len(result), 0, msg="Expect to match as the dataframe is empty"
        )
