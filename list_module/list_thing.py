class ListThing:

    def __init__(self, the_list, the_sum=None, min_max=(None,None),
                 max_diff=None):
        """
        Initializes instance of class ListThing

        :param the_list: list the object holds
        :type the_list: list
        :param the_sum: sum of the_list
        :type the_sum: float
        :param min_max: min and max of the_list 
        :type min_max: (Float, Float)
        :param max_diff: max difference between 2 adjacent elements in the_list
        :type max_diff: float
        :raises TypeError: if value given for the_list is not type list
        """
        self._the_list = the_list
        self.check_list()
        self.the_sum = the_sum
        self.min_max = min_max
        self.max_diff = max_diff

    def check_list(self):
        """
        Checks that self.the_list is type list, sets all variables
        to None if not type list (setting self.the_list to an empty list)

        :raises TypeError: if value given for the_list is not type list
        """
        if type(self.the_list) is not list:
            print("Given value is not type list and "
                  "is {}".format(type(self.the_list)))
            self.the_sum = None
            self.min_max = (None, None)
            self.max_diff = None
            raise TypeError("Given value is not type list and "
                            "is {}".format(type(self.the_list)))
   
    @property 
    def the_list(self):
        return self._the_list

    @the_list.setter
    def the_list(self, value):
        self._the_list = value
        self.check_list()

    def sum_list(self):
        """
        Sets self.the_sum to the sum of self.the_list

        :raises EmptyListError: if empty list is passed in
        :raises InfinityError: if list contains +/-infinity

        :return: void
        """
        try:
            import logging
            from custom_list_error import EmptyError, InfinityError
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
        logging.basicConfig(filename="./sum_list.log", filemode='w',
                            level=logging.DEBUG)
        if not self.the_list:
            logging.warning("List is empty: {}".format(self.the_list))
            raise EmptyError()
        try:
            logging.info("Trying to find the sum")
            the_sum = sum(self.the_list)
        except TypeError:
            logging.error("Incorect parameter type passed in: {} is "
                          "{}".format(self.the_list, type(self.the_list)))
            return None
        if float('inf') in self.the_list or float('-inf') in self.the_list:
            logging.warning("List contains infinite value")
            raise InfinityError()
        self.the_sum = float(the_sum)


    def max_difference(self):
        """
        Sets self.max_difference to the max difference between 
        adjacent values of self.the_list. Returns 0.0 if list
        only contains one value

        :raises EmptyListError: if empty list is passed in
        :raises InfinityError: if list contains +/-infinity

        :return: void
        """
        try:
            import logging
            from math import fabs
            from custom_list_error import EmptyError, InfinityError
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
        logging.basicConfig(filename='max_difference.log', filemode='w',
                            level=logging.DEBUG)
        if not self.the_list:
            logging.warning("List is empty: {}".format(self.the_list))
            raise EmptyError()
        curr_max = 0.0
        for index, entry in enumerate(self.the_list):
            try:
                num = float(entry)
            except (ValueError, TypeError):
                print("Value in list cannot be cast as float: {}".format(entry))
                return None
            if num == float('inf') or num == float('-inf'):
                logging.warning("List contains an infinite value")
                raise InfinityError()
            if index > 0:
                diff = fabs(entry - self.the_list[index-1])
                curr_max = max(curr_max, diff)
        logging.info("Setting self.max_diff")
        self.max_diff = curr_max


    def min_max_list(self):
        """
        Sets self.min_max to a tuple containing the min and max 
        values of self.the_list

        :raises EmptyListError: if empty list is passed in
        :raises InfinityError: if list contains +/-infinity

        :return: void
        """
        try:
            import logging
            from custom_list_error import EmptyError, InfinityError
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
        logging.basicConfig(filename='min_max_list.log', level=logging.DEBUG,
                            filemode='w')
        if not self.the_list:
            logging.warning("Empty list given")
            raise EmptyError()
        for val in self.the_list:
            try:
                num = float(val)
            except (ValueError, TypeError):
                print("Value in list cannot be cast as float: {}".format(entry))
                logging.debug("Erroneous type encountered: "
                              "{}".format(type(err)))
                return (None, None)
            if num == float('inf') or num == float('-inf'):
                raise InfinityError()
        my_min = min(self.the_list)
        my_max = max(self.the_list)
        logging.info("Setting self.min_max")
        self.min_max = (my_min, my_max)
