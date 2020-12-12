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

    def mogo_db_info(self) -> str:
        """Returns the information of mongo db connection."""
        return self.config['database']['mongo']['information']

    def mogo_db_name(self) -> str:
        """Returns the database name of mongo db."""
        return self.config['database']['mongo']['database']

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

    def bucket_access_key(self) -> str:
        """Returns the access key of bucket."""
        return self.config['bucket']['access_key']

    def bucket_secret_key(self) -> str:
        """Returns the secret key of bucket."""
        return self.config['bucket']['secret_key']

    def bucket_endpoint(self) -> str:
        """Returns the endpoint of bucket."""
        return self.config['bucket']['endpoint']

    def bucket_service_name(self) -> str:
        """Returns the service name of bucket."""
        return self.config['bucket']['service_name']


