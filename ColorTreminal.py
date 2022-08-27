from colorama import Fore, Style
from HelperHW2508 import *
from datetime import datetime


def main():
    print(Fore.RED + '1. Add to contact')
    print(Fore.YELLOW + '2. Delete to contact')
    print(Fore.MAGENTA + '3. Call to contact')
    print(Style.RESET_ALL)
    print('- - - - - - - - - - - - - - -')
    choose_user = input('Please write somethings you want :')
    # This Question ask for user and return to function the answer
    print(StringOrNum(choose_user))
    print('- - - - - - - - - - - - - - -')
    # turn on clock in terminal
    print(datetime.now())
    print('- - - - - - - - - - - - - - -')
    print(NumpyMethod([90, 100, 99], [90, 100, 50]))
    print('- - - - - - - - - - - - - - -')
    print(FdMethod('HW25.08.txt'))


if __name__ == '__main__':
    main()
