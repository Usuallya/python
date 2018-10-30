#python类的封装、继承和多态
#import people

from people import People
#1、继承的写法
class Student(People):
    # sum = 0
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age = age
    #     self.__score=0
    #     self.__class__.sum+=1

#派生类的构造函数需要传入父类需要的参数，然后调用父类的构造函数来完成初始化
    def __init__(self,school,name,age):
        self.school = school
        #注意：这里必须传入self，否则无法构造成功
        #这里相当于用类来调用了实例方法,是一个普通的调用，因此需要像
        #普通函数调用一样，传self
        People.__init__(self,name,age)

        #但是上面这样的构造方式并不推荐，开闭原则，比方说我们更换父类，那么派生类中
        #可能要修改很多地方，这不可取，而是应该采用下面这个方法
        super(Student,self).__init__(name,age)

    def do_homework(self):
        #可以再这里调用父类的同名方法
        super(Student,self).do_homework()
        print('english homework')

#现在student类中没有任何类变量和实例变量,而Student类继承了people中的类变量
#和实例变量,在实例化时，由于父类要求传入name和age，因此这里也必须传入
student=Student('bupt','wang',20)
# print(student.sum)
# print(Student.sum)
# print(student.name)
# print(student.age)
#对于方法的继承
student.get_name()
#注意：python允许多继承


#2、接下来是重载、多态相关内容
student1 = Student('swjtu','li',18)
#函数重名时，如果直接调用，那么直接使用当前对象的函数，这类似于C++
student1.do_homework()
