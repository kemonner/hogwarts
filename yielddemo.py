import time


def provider():
    # list = []
    for i in range(5):
        print('a')
        yield i
        # time.sleep(5)
        print('b')
    #     list.append(i)
    # return list


p = provider()
# print(p)
print(next(p))
print(next(p))
print(next(p))
# print(next(p))
# print(next(p))

