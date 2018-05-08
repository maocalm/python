

#  试图迭代一个数的错误； 一边循环一边计算；
def flatten (nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield  element
    except TypeError:
        print("type error ")
        yield  nested
nested =  [ [[1] ,2] ,3,4,[5 ,[6,7] , 8 ]]
print(list(flatten(nested)))

print("---------------------")

def flatten2(nested):
    try :
        try: nested + ''
        except TypeError :
            print('ex')
            pass
        else: raise  TypeError  #不走异常就走else
        # raise  TypeError
        for sublist in nested:
            print('for')
            for element in  flatten2(sublist):
                yield  element
    except TypeError:
        print("ppp")
        yield  nested  # 直接打印出了数组；

# nested =  [ [[1] ,2] ,3,4,[5 ,[6,7] , 8 ]]

# print(list(flatten2(nested)))

print(list(flatten2(['foo',6, ['bar', ['baz']]])))
