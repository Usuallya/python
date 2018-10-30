#函数的参数

#1、必须参数(参数列表中定义的参数是必须要传递的，不传递将会报错)
def add(x,y):
    return x+y
#2、关键字参数：通过指定关键字，可以任意指定参数的顺序
def minus(x,y):
    return x-y
c=minus(y=2,x=3)
print(c)

#3、默认参数
def multiply(x,y,mode=1):
    return x*(y+mode)
