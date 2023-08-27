from db.read import Read
from db.write import Write
from _quality_checks import QC, ALL
import initialiser
import os
import logging

current_file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(os.path.dirname(current_file_path))
relative_file_path = os.path.join(project_directory, "data_migrator/db/creds.yaml")

if __name__ == "__main__":
    # Initializing arg parser and logger
    args = initialiser.configure_parser()
    initialiser.configure_logger(args)
    logger = logging.getLogger(__name__)

    if args.test:
        from tests.run_tests import run_suite
        # Run unit tests
        run_suite()
        exit()

    logger.info("Data copying report")

    # Connect to dbs
    source_db = Read(relative_file_path, "SOURCE_DATABASE")
    target_db = Write(relative_file_path, "TARGET_DATABASE")

    # Fetch source data
    df_dict = {table_name: source_db.get_data(table_name) for table_name in ALL}

    # Quality checks and copying
    procedures = initialiser.initialise()

    for table_name, df in df_dict.items():
        for name, function in procedures.items():
            if name in QC and table_name in QC[name]:
                function(df, table_name)
        target_db.insert_data(table_name, df)

    msg = "Copying completed"
    print(msg)
    logging.info(msg)
