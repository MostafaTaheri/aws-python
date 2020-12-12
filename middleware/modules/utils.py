import re


class Tools:
    @staticmethod
    def packer(**kwargs):
        """ Make dictionary. """
        return kwargs

    @staticmethod
    def is_english(context: str) -> bool:
        """"Checks the content is English or not."""
        english_check = re.compile(r'[a-z]')
        return True if english_check.match(context) else False

    @staticmethod
    def is_invalid_character(context: str) -> bool:
        """"Checks the content contains non-word characters or not."""
        english_check = re.compile(r"\W")
        return True if english_check.findall(context) else False
