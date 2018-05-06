##简单生成器；
## 比较复杂的概念； 普通函数定义的迭代器；,yield ： 定义了生成器；

def flatten(nested):
    for sublist in nested :
        for element in sublist:
            yield element
nested =  [[1,2],[3,4],[5,6]]
# flatten(nested)

for  num in flatten(nested):
    print(num)
print(list(flatten(nested)))   # 对生成器进行迭代；