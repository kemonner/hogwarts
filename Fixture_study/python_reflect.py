class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is rating")


p = Person('jerry')
print(hasattr(p, 'eat'))  # hasattr判断实例有没有eat属性或者方法
f = getattr(p, 'eat')
f()  # 直接调用

print(getattr(p, 'age', 'finderror'))  # 去找age属性，如果没有，就输出自定义的默认值：'finderror'

print(getattr(p, 'name'))

