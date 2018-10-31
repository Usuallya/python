#装饰器
import time


def f1():
   print(time.time())
   print("this is a function")



def f2():
    #假设我们的每个函数都想要加上那个显示时间的功能，那么就得修改多个函数
    #但是按照开闭原则，对修改是封闭的，对扩展是开放的。我们应该拒绝修改，或者尽量减少修改。
    #此时应该怎么样？
   print('This is a function')

#为了解决类似问题，我们可以利用函数式编程的特点，专门编写一个函数，用来打印时间
#这个函数接受一个参数，是一个函数名（函数本身是一种对象，可以被传递）
def print_current_time(func):
   print(time.time())
   func()

#把之前的调用改为：print_current_time(f1)，即可。这种方式避免了修改函数内部

#但这个方法也是有问题的：
#关键在于，打印时间这个新增加的需求，并不能体现在各个函数本身上。
#这种做法和每次调用前人为加print没什么大的区别。

#装饰器能让我们新添加的业务逻辑可以和老函数绑定在一起，同时又不去更改老函数的内部实现

#装饰器只是一种模式，是我们自己可以实现的：
def f1():
    print("this is f1()")

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper



#对比上面的current_time函数，有什么区别吗？ 
#实际上唯一的区别就是使用了内部函数

#为什么这种模式称作装饰器呢？ decorator相当于装饰了
#实际功能函数wrapper，因此称作装饰器。但是装饰器如何能让
#新添加的业务逻辑能和老函数绑定在一起呢？

#python装饰器的语法糖：@符号
#@符号允许我们直接在原来的函数f1上，仅仅加个装饰器名字，就能
#直接用原来的调用方式去使用新功能。 这个语法糖让装饰器真正的起到了
#非常方便的作用。


#当f是带参数的函数时
#这里调用将会报错，因为decorator里的wrapper执行func时没有参数
#为了解决这种参数增加的问题，应该怎么做？
#可以采用函数传参时的可变参数：
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f(func_name):
    print('xx')

f('wang')

#装饰器所代表的思想：AOP面向切面编程
#如果我们想对某个被封装的代码进行行为修改，可以不用去
#修改代码本身，而是利用装饰器添加，在类似Flash这样的
#框架里，就大量应用了装饰器，来实现类似Spring MVC的
#Controller注解的形式