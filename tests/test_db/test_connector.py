import unittest
from sqlalchemy import create_engine
from db.connector import Connector
import os

current_file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(os.path.dirname(current_file_path))
relative_file_path = os.path.join(project_directory, "test_db/test_creds.yaml")


class TestDatabaseConnctor(unittest.TestCase):
    def setUp(self):
        config = {
            "USER": "test_user",
            "PASSWORD": "test_password",
            "HOST": "localhost",
            "PORT": 1433,
            "DATABASE": "test_db",
        }
        # Creating a mock engine to replicate the object
        self.mock_db_engine = create_engine(
            f"mssql+pymssql://{config['USER']}:{config['PASSWORD']}@{config['HOST']}:{config['PORT']}/{config['DATABASE']}"
        )

    def test_connect(self):
        db_connector = Connector(relative_file_path, "MOCK_CREDS")

        result = db_connector.connect()

        self.assertEqual(
            result.url,
            self.mock_db_engine.url,
            msg="Expecting to match as the credentials in both objects are identical",
        )

    def test_connect_wrong(self):
        db_connector = Connector(relative_file_path, "MOCK_CREDS_WRONG")
        result = db_connector.connect()
        result_assert = result.url == self.mock_db_engine.url
        self.assertFalse(
            result_assert,
            "Expecting False as the credentials do not match, thus the connection is not established correctly",
        )
