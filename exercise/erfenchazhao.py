def search (se , number  ,lower =0, up = None):

    if up is None :up= len(se)-1
    if lower ==up :
        assert  number==se[up]
        print(up)
        return up
    else:
        middle  = (lower+up) // 2   #
        if number>se[middle]:
            return search(se ,number , middle+1 ,up ) # return  没有返回；
        else:
            return search(se ,number ,lower ,middle)

seq = [34,67,88,99,104,149,190,566]
d= search(seq ,99)
print(d )


