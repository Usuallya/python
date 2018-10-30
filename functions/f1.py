#函数

#函数的返回值：1、return返回一个值 2、return 3、不写return，相当于默认return None
#4、返回多个值（甚至在函数里还能返回一个函数）
def print_code(code):
    print(code)
    return code
def damage(skill1,skill2):
    damage1=skill1+1
    damage2=skill2*2
    # 返回一个元组return (damage1,damage2)
    #返回两个值，只需要用逗号隔开就行了
    return damage1,damage2

#d1,d2接收返回值的方法称作序列解包的方法
d1,d2 = damage(1,2)
#这样调用的话，相当于默认转换成了元组
damages = damage(3,6)

print(damages)
print(type(damages))
print(d1,d2)

#序列解包
#下面的这三行赋值，可以通过序列解包来简化
a=1
b=2
c=3
#序列解包：
a,b,c=1,2,3
d=1,2,3
print(type(d))
#另一种形式的序列解包
a,b,c=d
print(a,b,c)
