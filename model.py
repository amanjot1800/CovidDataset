"""
Author: Amanjot Singh
Student number: 040956152
"""


class Record(object):
    """
    This class is a just a pure python object to store data. This class becomes a record object and
    holds information about a single row of data.
    """

    def __init__(self, lst):
        """
        This is the constructor for class record
        :param lst: A list of all the arguments is passed to the constructor to instantiate an object.
        """
        self._id = lst[0]
        self._pruid = lst[1]
        self._prname = lst[2]
        self._prnameFR = lst[3]
        self._date = lst[4]
        self._numconf = lst[5]
        self._numprob = lst[6]
        self._numdeaths = lst[7]
        self._numtotal = lst[8]
        self._numtoday = lst[9]
        self._ratetotal = lst[10]

    # These are the setters and getters for all the properties of this object.
    @property
    def id(self):
        return self._id

    @property
    def pruid(self):
        return self._pruid

    @property
    def prname(self):
        return self._prname

    @property
    def prnameFR(self):
        return self._prnameFR

    @property
    def date(self):
        return self._date

    @property
    def numconf(self):
        return self._numconf

    @property
    def numprob(self):
        return self._numprob

    @property
    def numdeaths(self):
        return self._numdeaths

    @property
    def numtotal(self):
        return self._numtotal

    @property
    def numtoday(self):
        return self._numtoday

    @property
    def ratetotal(self):
        return self._ratetotal

    @id.setter
    def id(self, value):
        self._id = value

    @pruid.setter
    def pruid(self, value):
        self._pruid = value

    @prname.setter
    def prname(self, value):
        self._prname = value

    @prnameFR.setter
    def prnameFR(self, value):
        self._prnameFR = value

    @date.setter
    def date(self, value):
        self._date = value

    @numconf.setter
    def numconf(self, value):
        self._numconf = value

    @numprob.setter
    def numprob(self, value):
        self._numprob = value

    @numdeaths.setter
    def numdeaths(self, value):
        self._numdeaths = value

    @numtotal.setter
    def numtotal(self, value):
        self._numtotal = value

    @numtoday.setter
    def numtoday(self, value):
        self._numtoday = value

    @ratetotal.setter
    def ratetotal(self, value):
        self._ratetotal = value

    def __str__(self):
        """
        This function overrides the default string function to print all details of the record.
        :return: Returns a single string of all the information
        """
        return "Id: \t\t" + str(self.id) + "\n" + \
               "pruid: \t\t" + str(self.pruid) + "\n" + \
               "prname: \t" + str(self.prname) + "\n" + \
               "prnameFR: \t" + str(self.prnameFR) + "\n" + \
               "date: \t\t" + str(self.date) + "\n" + \
               "numconf: \t" + str(self.numconf) + "\n" + \
               "numprob: \t" + str(self.numprob) + "\n" + \
               "numdeaths: \t" + str(self.numdeaths) + "\n" + \
               "numtotal: \t" + str(self.numtotal) + "\n" + \
               "numtoday: \t" + str(self.numtoday) + "\n" + \
               "ratetotal: \t" + str(self.ratetotal) + "\n"
