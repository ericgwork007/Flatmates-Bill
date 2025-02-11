from flat import Bill, Flatmates
from report import PdfReport

amt = float(input("Hey user, Enter the Bill amount: "))
prd = input("Enter the period stayed: ")
flmt1_name = input("Enter the name of Flatmate1: ")
flmt1_days_stayed = int(input("Enter the number of days stayed by Flatmate1: "))
flmt2_name = input("Enter the name of Flatmate2: ")
flmt2_days_stayed = int(input("Enter the number of days stayed by Flatmate2: "))

the_bill = Bill(amount = amt, period = prd)
fltmate1 = Flatmates(name = flmt1_name, no_of_days_stayed=flmt1_days_stayed)
fltmate2 = Flatmates(name = flmt2_name, no_of_days_stayed=flmt2_days_stayed)
print(fltmate1.pays(bill=the_bill.amount, flatmate2=fltmate2))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=fltmate1,flatmate2=fltmate2,bill=the_bill)



#OOP Principle:
#A class should be open for extension but closed for modification.