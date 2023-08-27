from db.connector import Connector
from sqlalchemy import MetaData, Table, select
import pandas as pd
import time
from sqlalchemy.exc import NoSuchTableError
import logging

logging = logging.getLogger(__name__)


class Read(Connector):
    def __init__(self, config, server):
        super().__init__(config, server)
        self.server = server

    def get_data(self, table_name):
        """
        Gets table data from SQL query

        :param table_name: table_name string
        :return: DataFrame, []
        """
        try:
            start_time = time.time()
            metadata = MetaData()
            table_data = Table(
                table_name, metadata, autoload=True, autoload_with=self.db
            )
            query = select([table_data])
            results = self.db.execute(query).fetchall()
            msg = f"Took {time.time()-start_time:.3f}s to fetch {table_name} data from {self.server}"
            print(msg)
            logging.info(msg)
            return pd.DataFrame(results)
        except NoSuchTableError:
            msg = f"Table with table name: {table_name} does not exist in database: {self.config['DATABASE']}"
            print(msg)
            logging.error(msg)
            return []
