import pandas as pd


def main_menu():
    """
        Simple Menu function.
    """
    print()
    print("|" + ("-"*33) + "|")
    print("|" + (f"{'Menu':^33}") + "|")
    print("|" + ("-"*33) + "|")
    print(f"{'|1. Show all Dataframe':<34}|")
    print(f"{'|2. Filter by specific header':<34}|")
    print(f"{'|3. Filter by row interval':<34}|")
    print(f"{'|4. Filter by multiple headers':<34}|")
    print(f"{'|5. Filter by interval and headers':<34}|")
    print(f"{'|0. Exit':<34}|")
    print("|" + ("-"*33) + "|")

# -----------------------------------------------------------------------------
# Converter funcition
# -----------------------------------------------------------------------------


def xls_converter(fileName):
    """ 
        This function uses the pandas lib to convert a
        .xls or .xlsx file to .csv file.

        Keyword arguments:
        fileName -- Complete name of file that should be converted. (String).
    """
    if '.xlsx' in fileName:
        newFileName = fileName[0:-5]

    elif '.xls' in fileName:
        newFileName = fileName[0:-4]

    else:
        return "error"

    data_xls = pd.read_excel(fileName, index_col=None)
    data_xls.to_csv(f'{newFileName}.csv', encoding='utf-8', index=False)
    csvFile = f'{newFileName}.csv'

    return csvFile

# -----------------------------------------------------------------------------
# Filter funcitions
# -----------------------------------------------------------------------------


def filter_by_specific_header(data):
    """ 
        This function uses the pandas lib to filter in
        a .csv file using a single header.

        Keyword arguments:
        data -- variable that contains all data from a .csv file (String).
    """
    print('Filter by header: \n')

    headers = dict(enumerate(data.columns.values))

    print('Header index:\n')
    for index, header in enumerate(data.columns.values):
        print(f'{index} - {header}')
    print()
    index = int(input('Select the header index: '))
    header = headers[index]
    print()
    print(data.loc[:, header])

    return


def show_all_dataframe(data):
    """ 
        This function uses the pandas lib to show all
        the data inside a .csv file.

        Keyword arguments:
        data -- variable that contains all data from a .csv file (String).
    """
    print(data)


def filter_by_interval(data):
    """ 
        This function uses the pandas lib to filter in
        a .csv file using a row interval.

        Keyword arguments:
        data -- variable that contains all data from a .csv file (String).
    """
    intervalStart = int(input('Select the start row: '))
    intervalEnd = int(input('Select the end row: '))

    print(data.loc[intervalStart:intervalEnd])


def filter_by_headers(data):
    """ 
        This function uses the pandas lib to filter in
        a .csv file using multiple headers.

        Keyword arguments:
        data -- variable that contains all data from a .csv file (String).
    """
    columnsValue = dict(enumerate(data.columns.values))

    print('Header index:\n')
    for index, header in enumerate(data.columns.values):
        print(f'{index} - {header}')
    print()

    numberOfHeaders = int(input('How many headers do you want to select: '))
    print()

    columns = list()
    for i in range(numberOfHeaders):
        index = int(input(f'Select the {i+1}º header index: '))
        columns.append(columnsValue[index])
    print()
    print(data.loc[:, columns])


def filter_by_interval_header(data):
    """ 
        This function uses the pandas lib to filter in
        a .csv file using multiple headers an a row interval.

        Keyword arguments:
        data -- variable that contains all data from a .csv file (String).
    """
    intervalStart = int(input('Select the start row: '))
    intervalEnd = int(input('Select the end row: '))

    columnsValue = dict(enumerate(data.columns.values))

    print('Header index:\n')
    for index, header in enumerate(data.columns.values):
        print(f'{index} - {header}')
    print()

    numberOfHeaders = int(input('How many headers do you want to select: '))
    print()

    columns = list()
    for i in range(numberOfHeaders):
        index = int(input(f'Select the {i+1}º header index: '))
        columns.append(columnsValue[index])
    print()
    print(data.loc[intervalStart:intervalEnd, columns])
