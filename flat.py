class Bill:
    """
    This object called Bill takes as input the amount and
    period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates():
    """
    This object type is used to create Flatmate objects
    which takes as input the names and the no. of days the
    flatmates lived in the flat, it also calculates the amount
    each flatmate has to pay using the pays method.
    """

    def __init__(self, name, no_of_days_stayed):
        self.name = name
        self.no_of_days_stayed = no_of_days_stayed

    def pays(self, bill, flatmate2):
        weight = self.no_of_days_stayed/(self.no_of_days_stayed+flatmate2.no_of_days_stayed)
        to_pay = bill * weight
        return to_pay
