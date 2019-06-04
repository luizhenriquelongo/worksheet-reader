import pandas as pd
from modules import *
from os import system, name
from time import sleep


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


fileName = 'exemplo2.csv'
error = False

if '.csv' in fileName:
    data = pd.read_csv(fileName)

else:
    csvFile = xls_converter(fileName)
    if csvFile == 'error':
        print('Invalid File Extension!')
        error = True
    else:
        data = pd.read_csv(csvFile)

if not error:

    while True:
        main_menu()
        option = int(input('Select an option: '))

        if option == 1:
            clear()
            show_all_dataframe(data=data)

        elif option == 2:
            clear()
            filter_by_specific_header(data=data)

        elif option == 3:
            clear()
            filter_by_interval(data=data)

        elif option == 4:
            clear()
            filter_by_headers(data=data)

        elif option == 5:
            clear()
            filter_by_interval_header(data=data)

        elif option == 0:
            clear()
            break

        else:
            clear()
            print('\nINVALID OPTION!')
            sleep(1)

input('Press <enter> to exit...')
