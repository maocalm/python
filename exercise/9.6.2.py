
class TestIterator :
    value = 0  # 必须进行初始化； 否则报错； 位置
    def __next__(self):
        self.value += 1
        if self.value >100 :raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))