while True :
    try :
        x = int (input('Enter the first number :'))
        y = int(input('enter the second number :'))
        value = x/y
        print('x/y is ' ,value)
    except  Exception as e :
        print('invalid input . please try again  ')
        print(e)

    else:
        break

    finally:
        print('llllllllll')

from warnings import warn ,filterwarnings
# warn('handdfadfaffasdfa' )   # 警告；
filterwarnings('ignore')
warn('hanwenmao')