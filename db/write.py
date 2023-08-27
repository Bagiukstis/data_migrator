from db.connector import Connector
import logging
import time

logging = logging.getLogger(__name__)


class Write(Connector):
    def __init__(self, config, server):
        super().__init__(config, server)
        self.server = server

    def insert_data(self, table_name, data):
        """
        Inserts a DataFrame to SQL database. If the same table already exists, it will be replaced.
        Chunksize of 1000 is a set limit by the SQL server

        :param table_name: table_name
        :param data: DataFrame
        :return: bool -> True if correct
        """
        try:
            if not data.empty:
                start_time = time.time()
                data.to_sql(
                    name=table_name,
                    con=self.db,
                    if_exists="replace",
                    index=False,
                    chunksize=1000,
                    method="multi",
                )
                msg = f"Took {time.time() - start_time:.3f}s to insert {table_name} data to {self.server}"
                print(msg)
                logging.info(msg)
                return True
        except AttributeError:
            msg = f"{table_name} can not be inserted to: {self.server}, as the data: {data} is not a DataFrame"
            print(msg)
            logging.error(msg)
            return False
