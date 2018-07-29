#列表练习
#定义列表时，其中元素可以是不同的数据类型
aa=[1,2,'心悦']
a=['新月打击','苍白之瀑','月至降临','月神冲刺']
#这里选取的是从倒数第一个开始到末尾，也就是只有最后一个元素
print(a[-1:])
#注意，同样是选取了最后一个元素，但是这两者的显示会有不同，前者会显示['月神冲刺']，即得到的是
#一个列表，而后者将只会得到字符串月神冲刺————————面试常见问题
print(a[-1])
#列表的相加
b=['点燃','虚弱']
print(a+b)
#列表的相乘
print(b*3) 
#这里将会重复三次

#列表没有减法：
#print(b-['点燃'])
#这里会报错

#元组练习
#元祖中的数据时不可变的
#定义元组可以直接用小括号
a=(1,2,3,4,5)
#定义元组时，其中每个元素都可以是不一样的类型
b=('a',12,3,True)
print(a)
#元组相加的操作
print(a+b)
#类型是class tuple
print(type((1,2,3)))
#注意，这样执行之后将不是元组
print(type((1)))
print(type(('strrrrr')))

