import yaml


class LoadConfig:
    """Loads information of yaml config file.

    Example:
        config = LoadConfig()
        mongo_url = config.mogo_db_info()
    """
    def __init__(self):
        self.file = open("config.yml")
        self.config = yaml.load(self.file, Loader=yaml.FullLoader)

    def api_url(self, section_name: str) -> str:
        """Returns the information of API url."""
        return self.config['api'][section_name]['url']

    def logging_info(self) -> str:
        """Returns the file name of log file."""
        return self.config['logging']['file_name']

    def logging_mode(self) -> str:
        """Returns the mode of log file."""
        return self.config['logging']['mode']

    def logging_format(self) -> str:
        """Returns the format of log file."""
        return self.config['logging']['format']

    def logging_date_format(self) -> str:
        """Returns the date format of log file."""
        return self.config['logging']['date_format']


