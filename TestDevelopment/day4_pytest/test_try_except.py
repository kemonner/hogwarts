try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print("您输入的两个数相除的结果是：", c)
# except (ExceptionType, Argument):
except (ValueError, ArithmeticError):
    print("程序发生数字格式异常，算数异常之一")
except:
    print("其他异常")
print("继续执行")
