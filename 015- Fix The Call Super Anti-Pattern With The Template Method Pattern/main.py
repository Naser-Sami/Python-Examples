
from abc import ABC, abstractmethod


class Reports(ABC):

    @abstractmethod
    def make_report_body(self):
        ...

    def make_report(self):
        print("\n** REPORT HEADING **")
        print("Company: " + self.company)
        print("********************")
        self.make_report_body()


class SalesReport(Reports):
    def __init__(self, company, sales):
        self.company = company
        self.__sales = sales

    def make_report_body(self):
        print("Sales: "  + str(self.__sales))


class CostsReport(Reports):
    def __init__(self, company, costs) -> None:
        self.company = company
        self.__costs = costs

    def make_report_body(self):
        print("Costs: "  + str(self.__costs))

sales_report = SalesReport('Google', 100000)
sales_report.make_report()

costs_report = CostsReport('Amazon', 40000)
costs_report.make_report()
