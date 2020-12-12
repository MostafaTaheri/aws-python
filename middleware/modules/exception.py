class CustomException(Exception):
    """Customise error exception.

    Example:
        CustomException(101, 'There is no any record')
    """
    def __init__(self, fault_code, fault_message):
        super(Exception, self).__init__(fault_message)
        self.fault_code = fault_code
        self.fault_message = fault_message
