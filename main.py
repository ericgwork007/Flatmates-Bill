import webbrowser

from fpdf import FPDF


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

class PdfReport:
    """
    This object generates a pdf with the names of the flatmates
    and the amount each of the flat mate finally has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill.amount, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill.amount, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image("house icon.png", w=30, h=30)

        # Add the title of the pdf
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)  # Use 'txt' instead of 'text'

        #Add the Period of the Bill.
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)  # Adjusted height

        # Add the bill amount and details of flatmate 1.
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=50, h=40, txt=flatmate1_pay, border=0, ln=1)  # Adjusted height

        # Add the bill amount and details of flatmate 2.
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=50, h=40, txt=flatmate2_pay, border=0, ln=1)  # Adjusted height

        pdf.output(self.filename)

        webbrowser.open(self.filename)

amt = float(input("Hey user, Enter the Bill amount: "))
prd = input("Enter the period stayed: ")
flmt1_name = input("Enter the name of Flatmate1: ")
flmt1_days_stayed = int(input("Enter the number of days stayed by Flatmate1: "))
flmt2_name = input("Enter the name of Flatmate2: ")
flmt2_days_stayed = int(input("Enter the number of days stayed by Flatmate1: "))

the_bill = Bill(amount = amt, period = prd)
fltmate1 = Flatmates(name = flmt1_name, no_of_days_stayed=flmt1_days_stayed)
fltmate2 = Flatmates(name = flmt2_name, no_of_days_stayed=flmt2_days_stayed)
print(fltmate1.pays(bill=the_bill.amount, flatmate2=fltmate2))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=fltmate1,flatmate2=fltmate2,bill=the_bill)