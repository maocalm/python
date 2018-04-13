x =1
# while x <10 :
#     print(x)
#     x+=1
# numbers  = [2,3,5,6,7,8]
# for number  in numbers:
#     print(number)

# d  = {'x' : 1  , 'y' : 2  , 'z':3  , 'a' :4 , 'b':5  }
#
# for  key in d :
#      print(key , d[key])
# xxx =  ["this is a  gooog man " ]
#
# for index , string  in enumerate(xxx):
#     if  'i' in  string :
#         xxx[index]  = 'l'
#
# print(xxx)


# 男孩女孩匹配
# girls  = ['alice' , 'bernice' ,'clarice']
# boys = ['chars' ,  'around'  ,  'bob']
# var = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
# print(var)

#
# let = {}
# print(let)
# let.setdefault("han" , 0)
# print(let.setdefault("han" , 0) )
# print( let.setdefault("hanw" , []).append('wen') )
# print(let)
# let.setdefault(girls[0] ,[]).append(girls[0])
# print(let)
# print(let.setdefault(girls[0]), [] )
# let.append(girls[0])


#
# print('========================')
# girlss  = ['alice' , 'bernice' ,'clarice']
# boyss = ['chars' ,  'around'  ,  'bob']
# letterGirls = {}
# for girl in girls :
#     letterGirls.setdefault(girl[0] , [] ).append(girl)
# print(letterGirls)
#
# print('========================')
#
# print([b + '+' +g  for b in boys for g in letterGirls[b[0]]] )
# print('========================2')

# n = 'hanwen'
# def change (n):
#     print(n+"mao")
# def change2(n):
#     # n[0] = 'w' # 自负串不可变
#     return
# change(n)
# print(n)
#
# print(n[0])
# change2(n)
# print(n)



#
# names  = ['1' ,'2' ,'3' ,'4']
# n = names
# n1 = names[:]
#
# if  (n is names) :
#     print('true')
# else:
#     print('false')
#
# print(n1 is names)




assert 2+2 ==2*2
