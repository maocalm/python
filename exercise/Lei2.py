class Member:
    member = 0

    def init(self):
        Member.member += 1


m1 = Member()
m2 = Member()

m1.init()
print(m1.member)

m2.init()
print(m2.member)

m1.member ="wenmao"
print(m1.member)

print(m1.init()) #  没有返回值
print(m2.init()) #灭有返回值
print(m1.member)  #遮盖类级变量
print(m2.member)