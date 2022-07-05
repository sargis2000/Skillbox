class Property:
    """
        This is Base class

        Args:
            worth(int): Cost of item
        Methods:
            cross
    """
    def __init__(self, worth):
        self.worth = worth

    def cross(self):
        """
        Initializing the function
        :return: None
        """
        pass


class Apartment(Property):
    """
        Class Apartment. Parent:Property

        Args:
            worth(int): Cost of item
        """
    def __init__(self, worth):
        super().__init__(worth)

    def cross(self):
        """
        Overloading
        :return:int  Tax  of worth
        """

        return self.worth / 1000


class Car(Property):
    """
            Class Car. Parent:Property

            Args:
                worth(int): Cost of item

            Methods:
                cross
    """
    def __init__(self, worth):
        super().__init__(worth)

    def cross(self):
        """
        Overloading
        :return:int  Tax  of worth
        """
        return self.worth / 200


class CountryHouse(Property):
    """
            Class CountryHouse. Parent:Property

            Args:
                worth(int): Cost of item

            Methods:
                cross
            """
    def __init__(self, worth):
        super().__init__(worth)

    def cross(self):
        """
        Overloading
        :return:int  Tax  of worth
            """
        return self.worth / 500


class Main:
    """
    From where  program start

    """
    def __init__(self):
        self.mon_count = int(input('количество денег :'))
        self.tax_house = CountryHouse(int(input('стоимость имущества CountyHouse :'))).cross()
        self.tax_apart = Apartment(int(input('стоимость имущества Apartment :'))).cross()
        self.tax_car = Car(int(input('стоимость имущества Car :'))).cross()
        self.tax = self.tax_car + self.tax_apart + self.tax_house
        print(f"Your tax  ={self.tax}")
        if self.tax > self.mon_count:
            print(f'You  need {self.tax - self.mon_count}')


Main()





