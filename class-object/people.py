class People():
    #people不制定构造函数，会自动产生默认构造函数
    sum = 0 
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def get_name(self):
        print(self.name)

    #多态性的测试
    def do_homework(self):
        print("this is a parent method")