from random import randint, choice


class Karma:
    """
        Attributes
    --------
    __max_val : int
        karma's maximum value
    __exceptions : list
        Errors list

        Methods
    ------
    one_day(self):
        karma's maximum values - random number from 1 to 7 and
            rese Exception in 1 to 10

    """
    def __init__(self):
        """
        Sets all necessary attributes for the person object.
        And Do main functionality
        """
        self.__max_val = 500
        self.__exceptions = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
        with open('karma.log', 'w') as file:
            while True:
                x = self.one_day()
                if not x:
                    break
                elif x in self.__exceptions:
                    file.write(str(x) + '\n')

    def one_day(self):
        """
        karma's maximum values - random number from 1 to 7 and
            rese Exception in 1 to 10

        :return: True if maximum value high then 0
                        else return False
                or return Exception Arguments
        """
        print(self.__max_val)
        self.__max_val -= randint(1, 7)
        try:
            if randint(1, 10) == 9:
                raise Exception(choice(self.__exceptions))
        except Exception as Exc:
            return Exc.args[0]
        return True if self.__max_val > 0 else False


Karma()
help(Karma)






