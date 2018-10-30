#面向对象
#有意义的面向对象代码：不是说出现了类就是面向对象

#类的命名：第一个字母大写，变量的两个单词之间一般用下划线作链接，但是
#类名不建议这么做
#类的括号中的参数代表基类名
class Student():
    #在类的内部可以做的事情，定义数据成员：
    #这里是类变量，这里的类变量相当于是静态变量
    name=''
    age=0
    sum1=0
    #定义构造函数,python的构造函数也可以重载：
    def __init__(self,name,age):
        #构造函数不能有返回值（None除外）
        #构造函数中可以初始化 实例变量，实例变量才是python类中
        #真正的成员变量
        self.name=name
        self.age=age
        self.sex='男'

    def __init__(self,name):
        self.name=name
        self.age=0
        self.sex='女'
        print(name)

    # def __init__(self):
    #     #仍然需要通过self来访问成员变量
    #     self.name='111'
    #     self.age=2
    #定义实例方法,类中的函数必须加上形参self，这相当于c++里的this指针
    #实例方法：第一个参数必须是传入self
    #实例方法通常是用来操作实例变量的，要操作类变量，可以定义类方法
    #实际上也就是相当于静态成员函数
    def print_file(self):
        #在这里引用类内部变量name 和 age，需要通过self来引用
        print('name='+self.name)
        print('age='+str(self.age))
        #在类内部访问类变量的方法：
        self.__class__.name='lis'
    
    #定义类方法，使用装饰器来修饰函数，就能让他成为一个类方法
    @classmethod
    def plus_sum(cls):
        #类方法中操作类变量，就直接使用cls
        cls.sum1+=1
        print(cls.sum1)

    #类方法本来就相当于静态成员函数了，但是python居然还有静态方法。。
    @staticmethod
    def staticAdd():
        #注意：静态方法不用传self或者cls
        #静态方法可以通过类名访问类变量，但是不能访问实例变量
        print('this is a statics method')


#使用类中的Print_file函数，首先实例化一个类对象：
# student = Student()
# student.print_file()


student1= Student('wang')
#在我们通过实例去访问变量时，python首先查看实例变量列表，然后
#查看类变量，如果还没有找到，那么就到当前类的父类中找
print(student1)
# student1.print_file()

#调用类方法：
Student.plus_sum()


#类变量
# print(Student.name)
#可以通过内置变量__dict__来查看变量stident1的成员
# print(student1.__dict__)
# print(Student.__dict__)
# #可以直接访问数据成员？
#print(student.name)
# python中方法和函数的区别：方法是设计层面上的称呼  函数是程序运行、过程式的一种称谓
# 对于类中的成员函数，建议称作方法。



