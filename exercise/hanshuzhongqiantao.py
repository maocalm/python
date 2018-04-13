def multiplier (factor):
    def multiplipyByFactor (number):
        return number*factor
    return multiplipyByFactor


double  = multiplier(2)
print(double(5))


for i in range(0,6):
    print(i)