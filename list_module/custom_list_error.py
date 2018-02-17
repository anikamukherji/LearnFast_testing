class CustomListError(BaseException):
    """
    Custom set of exceptions for this list module
    """
    def __init__(self, message=""):
        """
        Creating an instance of an exception

        :param message: optional message to explain exception
        :type message: string
        """
        self.message = message


class EmptyError(CustomListError):
    """
    Exception to be thrown if empty list is passed in
    """
    pass


class InfinityError(CustomListError):
    """
    Exception to be thrown if given list contains +/- infinity
    """
    pass
