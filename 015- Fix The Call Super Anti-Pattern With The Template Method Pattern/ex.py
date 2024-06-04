# 
#  We might implement the above functionality like this, but we would have 
#  duplicated code in the make_report methods.  We might then try to factor 
#  out this code duplication by using the call super anti-pattern above.  A 
#  better approach would be to use the template method design pattern.
#

class SalesReports:
    def __init__(self, company, sales):
        self.__company = company
        self.__sales = sales

    def make_report(self):
        print("\n** REPORT HEADING **")
        print("Company: " + self.__company)
        print("********************")
        print("Sales: "  + str(self.__sales))


class CostsReports:
    def __init__(self, company, costs):
        self.__company = company
        self.__costs = costs

    def make_report(self):
        print("\n** REPORT HEADING **")
        print("Company: " + self.__company)
        print("********************")
        print("Costs: "  + str(self.__costs))


sales_reports = SalesReports('Google', 30000)
sales_reports.make_report()

costs_reports = CostsReports('Amazon', 50000)
costs_reports.make_report()
