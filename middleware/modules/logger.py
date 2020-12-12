import logging

from config import LoadConfig


class Logging:
    """Customise log information.

    Example:
        log = Logging()
        log.error(message=Exception)
    """
    def __init__(self):
        self.config = LoadConfig()
        self._basic_config()

    def error(self, message):
        """Records error log."""
        logging.error(message)

    def warning(self, message):
        """Records warning log."""
        logging.warning(message)

    def info(self, message):
        """Records info log."""
        logging.info(message)

    def _basic_config(self):
        """Sets basic config for logging."""
        logging.basicConfig(filename=self.config.logging_info(),
                            filemode=self.config.logging_mode(),
                            format=self.config.logging_format(),
                            datefmt=self.config.logging_date_format())
