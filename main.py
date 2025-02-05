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

    def pays(self, bill):
        return bill.amount/2

class GeneratePdf:
    """
    This object generates a pdf with the names of the flatmates
    and the amount each of the flat mate finally has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount = 1200, period = "March 2024")
john = Flatmates(name = "John", no_of_days_stayed=15)
mary = Flatmates(name = "Mary", no_of_days_stayed=20)
print(john.pays(bill=the_bill))
