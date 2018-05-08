a = ' ' + 'jun'
print(a)

a = ' '+ 'fun'
print(a)

# a = 1 + 'e'
# print(a)


g =  (x*x for x in range(6))
print(g)
for i  in range(6):  # 生成留个数
    print(next(g))
