import yaml
from sqlalchemy import create_engine
import logging

logging = logging.getLogger(__name__)


class Connector(object):
    def __init__(self, config, server):
        config_parsed = self.yml_parser(config)
        self.config = {
            "USER": config_parsed[server]["USER"],
            "PASSWORD": config_parsed[server]["PASSWORD"],
            "HOST": config_parsed[server]["HOST"],
            "DATABASE": config_parsed[server]["DATABASE"],
            "PORT": config_parsed[server]["PORT"],
        }
        self.db = self.connect()

    def yml_parser(self, config):
        """
        Opens and parses a specified config file to a dict

        :param config: Path to config
        :return: Dict
        """
        with open(config, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)

    def connect(self):
        """
        Connects to the Microsoft SQL engine using specified credentials
        """
        db = create_engine(
            f'mssql+pymssql://{self.config["USER"]}:{self.config["PASSWORD"]}@{self.config["HOST"]}:{self.config["PORT"]}/{self.config["DATABASE"]}'
        )
        return db
