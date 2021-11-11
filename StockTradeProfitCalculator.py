'''
Please make sure you use the PEP guide for naming conventions in your submission
- detailed guide: https://www.python.org/dev/peps/pep-0008/
- some examples: https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names

This assignment is heavily based on
A Currency Converter GUI Program - Python PyQt5 Desktop Application Development Tutorial
- GitHub: https://github.com/DarBeck/PyQT5_Tutorial/blob/master/currency_converter.py
- YouTube: https://www.youtube.com/watch?v=weKpTw1SjM4 - detailed explanaton

- Layout
    - I would suggest QGridLayout
    - Use a QCalendarWidget which you will get from Zetcode tutorial called "Widgets" http://zetcode.com/gui/pyqt5/widgets/

PyCharm Configuration Options
- Viewing Documentation when working with PyCharm https://www.jetbrains.com/help/pycharm/viewing-external-documentation.html
- Configuring Python external Documenation on PyCharm https://www.jetbrains.com/help/pycharm/settings-tools-python-external-documentation.html
'''

# standard imports
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from decimal import Decimal


class StockTradeProfitCalculator(QDialog):
    '''
    Provides the following functionality:

    - Allows the selection of the stock to be purchased
    - Allows the selection of the quantity to be purchased
    - Allows the selection of the purchase date
    - Displays the purchase total
    - Allows the selection of the sell date
    - Displays the sell total
    - Displays the profit total
    - Additional functionality

    '''

    def __init__(self):
        '''
        This method requires substantial updates
        Each of the widgets should be suitably initalized and laid out
        '''
        super().__init__()

        # setting up dictionary of stocks
        self.data = self.make_data()
        # sorting the dictionary of stocks by the keys. The keys at the high level are dates, so we are sorting by date
        self.stocks = sorted(self.data.keys())

        # the following 2 lines of code are for debugging purpose and show you how to access the self.data to get dates and prices
        # print all the dates and close prices for AAL
        print("all the dates and close prices for AAL", self.data['AAL'])
        # print the close price for AAL on 12/2/2013
        print("the close price for AAL on 12/2/2013", self.data['AAL'][QDate(2013, 2, 12)])

        # The data in the file is in the following range
        #  first date in dataset - 7th Feb 2013
        #  last date in dataset - 8th Feb 2018
        # When the calendars load we want to ensure that the default dates selected are within the date range above
        #  we can do this by setting variables to store suitable default values for sellCalendar and buyCalendar.
        self.sellCalendarDefaultDate = sorted(self.data['AAL'].keys())[
            -1]  # Accessing the last element of a python list is explained with method 2 on https://www.geeksforgeeks.org/python-how-to-get-the-last-element-of-list/
        print("self.sellCalendarStartDate", self.sellCalendarDefaultDate)
        # self.buyCalendarDefaultDate
        # print("self.buyCalendarStartDate", self.buyCalendarDefaultDate)

        # Create the main layout of the form
        verticalLayout = QVBoxLayout()

        # Create the main layout of the form
        self.setWindowTitle("Ass 1 - StockTradeProfitCalculator - OguzSarac - 2988989")

        # Create QLabel for stock purchased
        stockPurchasedHLayout = QHBoxLayout()  # Horizontal layout where widgets will be placed
        self.stockPurchasedLabel = QLabel("Stock Purchased: ")

        stockPurchasedHLayout.addWidget(self.stockPurchasedLabel)  # Widget added to stockPurchasedHLayout layout

        # Create QComboBox and populate it with a list of stocks
        self.stockPurchasedComboBox = QComboBox()  # Combobox is created
        self.stockPurchasedComboBox.setFixedWidth(320)  # Widget's pinned width is set to 320
        self.stockPurchasedComboBox.addItems(list(i for i in self.stocks))  # Data from self.stocks is added to combobox
        stockPurchasedHLayout.addStretch()
        stockPurchasedHLayout.addWidget(self.stockPurchasedComboBox)  # Widget added to stockPurchasedHLayout layout

        verticalLayout.addLayout(stockPurchasedHLayout)  # Layout added to verticalLayout layout

        # Create QLabel for purchaseDate

        purchaseDateHLayout = QHBoxLayout()  # Horizontal layout where widgets will be placed

        self.purchaseDateLabel = QLabel("Purchase Date: ")

        # Create CalendarWidgets for selection of purchase date

        self.purchaseDateCalendarWidget = QCalendarWidget()
        purchaseDateHLayout.addWidget(self.purchaseDateLabel)  # Widget added to stockPurchasedHLayout layout
        purchaseDateHLayout.addStretch()
        purchaseDateHLayout.addWidget(self.purchaseDateCalendarWidget)
        self.purchaseDateCalendarWidget.setFixedWidth(320)  # Widget's pinned width is set to 320
        verticalLayout.addLayout(purchaseDateHLayout)  # Layout added to verticalLayout layout

        # Create QLabel for quantity purchased

        quantityPurchasedHLayout = QHBoxLayout()  # Horizontal layout where widgets will be placed

        self.quantityPurchasedLabel = QLabel("Quantity Purchased: ")

        # Create QSpinBox to select stock quantity purchased

        self.stockQuantitySpinBox = QSpinBox()
        self.stockQuantitySpinBox.setRange(1, 1000000)  # The spinbox value range - Range is a changeable
        self.stockQuantitySpinBox.setFixedWidth(320)  # Widget's pinned width is set to 320
        quantityPurchasedHLayout.addWidget(self.quantityPurchasedLabel)
        quantityPurchasedHLayout.addStretch()
        quantityPurchasedHLayout.addWidget(self.stockQuantitySpinBox)  # Widget's pinned width is set to 320

        verticalLayout.addLayout(quantityPurchasedHLayout)  # Layout added to verticalLayout layout

        # Create QLabels to show the stock purchase total

        purchaseTotalHLayout = QHBoxLayout()  # horizontal layout where widgets will be placed
        self.purchaseTotalLabel = QLabel("Purchase Total: ")

        self.purchaseDateCalendarWidget.setMinimumDate(QDate(2013, 2, 8))  # Set the minimum date of the calendar widget
        self.purchaseDateCalendarWidget.setMaximumDate(QDate(2018, 2, 7))  # Set the maximum date of the calendar widget
        # the total value is calculated
        self.purchaseTotal = QLabel(str(self.data[self.stockPurchasedComboBox.currentText()][
                                            self.purchaseDateCalendarWidget.selectedDate()] * self.stockQuantitySpinBox.value()))
        purchaseTotalHLayout.addWidget(self.purchaseTotalLabel)
        purchaseTotalHLayout.addStretch()
        purchaseTotalHLayout.addWidget(self.purchaseTotal)
        verticalLayout.addLayout(purchaseTotalHLayout)  # Layout added to verticalLayout layout

        # create QLabel for sell date

        sellDateHLayout = QHBoxLayout()  # horizontal layout where widgets will be placed

        self.sellDateLabel = QLabel("Sell Date: ")

        # create CalendarWidgets for selection of sell date
        self.sellDateCalendarWidget = QCalendarWidget()
        self.sellDateCalendarWidget.setMinimumDate(QDate(2013, 2, 8))  # Set the minimum date of the calendar widget
        self.sellDateCalendarWidget.setMaximumDate(QDate(2018, 2, 7))  # Set the maximum date of the calendar widget
        self.sellDateCalendarWidget.setFixedWidth(320)  # Widget's pinned width is set to 320

        sellDateHLayout.addWidget(self.sellDateLabel)
        sellDateHLayout.addStretch()
        sellDateHLayout.addWidget(self.sellDateCalendarWidget)

        verticalLayout.addLayout(sellDateHLayout)  # Layout added to verticalLayout layout

        # create QLabels to show the stock sell total

        sellTotalHLayout = QHBoxLayout()

        self.sellTotalLabel = QLabel("Sell Total: ")
        # sell total is calculated
        self.sellTotal = QLabel(str(self.data[self.stockPurchasedComboBox.currentText()][
                                        self.sellDateCalendarWidget.selectedDate()] * self.stockQuantitySpinBox.value()))
        sellTotalHLayout.addWidget(self.sellTotalLabel)
        sellTotalHLayout.addStretch()
        sellTotalHLayout.addWidget(self.sellTotal)
        verticalLayout.addLayout(sellTotalHLayout)  # Layout added to verticalLayout layout

        # Create QLabels to show the stock profit total

        profitTotalHLayout = QHBoxLayout()
        self.profitTotalLabel = QLabel("Profit Total: ")

        # profit total is calculated
        self.profitTotal = QLabel(str(float(self.sellTotal.text()) - float(self.purchaseTotal.text())))
        profitTotalHLayout.addWidget(self.profitTotalLabel)
        profitTotalHLayout.addStretch()
        profitTotalHLayout.addWidget(self.profitTotal)

        verticalLayout.addLayout(profitTotalHLayout)  # Layout added to verticalLayout layout

        verticalLayout.addStretch()
        self.calculateButton = QPushButton("Calculate")  # Calculation button is created
        self.calculateButton.clicked.connect(
            self.calculateFunction)  # The function that will run when the calculation button is pressed is set.
        verticalLayout.addWidget(self.calculateButton)  # Widget added to verticalLayout layout
        self.setLayout(verticalLayout)  # the layout of the window is set to vertical layout

    def calculateFunction(self):

        # values are recalculated
        self.purchaseTotal.setText(str(self.data[self.stockPurchasedComboBox.currentText()][
                                           self.purchaseDateCalendarWidget.selectedDate()] * self.stockQuantitySpinBox.value()))
        self.sellTotal.setText(str(self.data[self.stockPurchasedComboBox.currentText()][
                                       self.sellDateCalendarWidget.selectedDate()] * self.stockQuantitySpinBox.value()))
        self.profitTotal.setText(str(float(self.sellTotal.text()) - float(self.purchaseTotal.text())))

    def updateUi(self):
        '''
        This requires substantial development
        Updates the Ui when control values are changed, should also be called when the app initializes
        :return:
        '''
        try:
            print("")
            # get selected dates from calendars

            # perform necessary calculations to calculate totals

            # update the label displaying totals
        except Exception as e:
            print(e)

    ################ YOU DO NOT HAVE TO EDIT CODE BELOW THIS POINT  ########################################################

    def make_data(self):
        '''
        This code is complete
        Data source is derived from https://www.kaggle.com/camnugent/sandp500/download but use the provided file to avoid confusion

        Converts a CSV file to a dictonary fo dictionaries like

            Stock   -> Date      -> Close
            AAL     -> 08/02/2013 -> 14.75
                    -> 11/02/2013 -> 14.46
                    ...
            AAPL    -> 08/02/2013 -> 67.85
                    -> 11/02/2013 -> 65.56

        Helpful tutorials to understand this
        - https://stackoverflow.com/questions/482410/how-do-i-convert-a-string-to-a-double-in-python
        - nested dictionaries https://stackoverflow.com/questions/16333296/how-do-you-create-nested-dict-in-python
        - https://www.tutorialspoint.com/python3/python_strings.htm
        :return: a dictionary of dictionaries
        '''
        file = open("./all_stocks_5yr.csv",
                    "r")  # open a CSV file for reading https://docs.python.org/3/library/functions.html#open
        data = {}  # empty data dictionary
        file_rows = []  # empty list of file rows
        # add rows to the file_rows list
        for row in file:
            file_rows.append(row.strip())  # https://www.geeksforgeeks.org/python-string-strip-2/
        print("len(file_rows):" + str(len(file_rows)))

        # get the column headings of the CSV file
        row0 = file_rows[0]
        line = row0.split(",")
        column_headings = line
        print(column_headings)

        # get the unique list of stocks from the CSV file
        non_unique_stocks = []
        file_rows_from_row1_to_end = file_rows[1:len(file_rows) - 1]
        for row in file_rows_from_row1_to_end:
            line = row.split(",")
            non_unique_stocks.append(line[6])
        stocks = self.unique(non_unique_stocks)
        print("len(stocks):" + str(len(stocks)))
        print("stocks:" + str(stocks))

        # build the base dictionary of stocks
        for stock in stocks:
            data[stock] = {}

        # build the dictionary of dictionaries
        for row in file_rows_from_row1_to_end:
            line = row.split(",")
            date = self.string_date_into_QDate(line[0])
            stock = line[6]
            close_price = line[4]
            # include error handeling code if close price is incorrect
            data[stock][date] = float(close_price)
        print("len(data):", len(data))
        return data

    def string_date_into_QDate(self, date_String):
        '''
        This method is complete
        Converts a data in a string format like that in a CSV file to QDate Objects for use with QCalendarWidget
        :param date_String: data in a string format
        :return:
        '''
        date_list = date_String.split("-")
        date_QDate = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return date_QDate

    def unique(self, non_unique_list):
        '''
        This method is complete
        Converts a list of non-unique values into a list of unique values
        Developed from https://www.geeksforgeeks.org/python-get-unique-values-list/
        :param non_unique_list: a list of non-unique values
        :return: a list of unique values
        '''
        # intilize a null list
        unique_list = []

        # traverse for all elements
        for x in non_unique_list:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
                # print list
        return unique_list


# This is complete
if __name__ == '__main__':
    app = QApplication(sys.argv)
    currency_converter = StockTradeProfitCalculator()
    currency_converter.show()
    sys.exit(app.exec_())
