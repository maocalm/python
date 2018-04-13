x=1
scope = vars()
print(scope)



xx= 1
def change_global():
    # global xx
    xx2 = xx+1
change_global()

print(xx)



