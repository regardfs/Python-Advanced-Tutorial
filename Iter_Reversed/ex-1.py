# iter and reversed

class NumRange(object):

    def __init__(self, start, end, stride):
        self.start = start
        self.end = end
        self.stride = stride

    def __iter__(self):
        num = self.start
        while num <= self.end:
            yield num
            num += self.stride

    def __reversed__(self):
        num = self.end
        while num >= self.start:
            yield num
            num -= self.stride
# test
for x in reversed(NumRange(0.0,5.0,0.5)):
    print x

for x in NumRange(0.0,5.0,0.5):
    print x