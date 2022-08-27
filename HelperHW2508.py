import numpy as np
import fs
def StringOrNum(question):
    """for this function i check if the input is string or number"""
    if question.isdigit():
        # if the input is number i check the length
        print(f'The length input is :{len(question)}')
        # check if the number is even or not
        if int(question) % 2 == 0:
            print('even')
        else:
            print('not even')
        # check if input dividing 7 without remnant
        if int(question) % 7 == 0:
            print('The input dividing in 7')
        else:
            print(f'The remnant {int(question) % 7}')
        return True
    else:
        return 'The input is string'


def NumpyMethod(arry1, arry2):
    """this function takes two grade and announces who won """
    max_mun = np.maximum(arry1, arry2)
    return f'the winner is  {max_mun}'


def FdMethod(path):
    pass

