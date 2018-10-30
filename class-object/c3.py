#访问控制和可见性
class Student():
    #python中所有的变量，默认是公有的
    #要想让一个变量或者方法变为私有，需要给他的名字前面加__

    sum=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        #这里把成绩改为私有
        self.__score=0
    #公有实例方法
    def print_file(self):
        print(self.name)
        print(self.age)
        print(self.__score)

    def __getScore(self):
        return self.__score
    #打分函数
    def marking(self,score):
        self.__getScore()
        if(score<0):
            print('不能打负分')
            return
        self.__score=score

student =Student('wang',25)
student.marking(95)
student.print_file()


#注意：尽管我们已经把score设置为私有，但是通过以下方式依然可以赋值和访问__score
student.__score=200
#这是因为python作为动态语言，这里相当于它创建了一个新的__score，而不是类中的那个
#实例变量__score
print(student.__score)
#_student__score就是我们的私有变量，__score是刚才它自动新增的变量
print(student.__dict__)