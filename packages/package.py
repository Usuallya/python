#python项目的组织结构：
#包——一个或多个模块——一个或多个类-函数-变量
#一个模块的物理表现，实际上就是一个py文件，一个包物理上就是
#以文件夹的形式来组织的。

#包天然带有命名空间的功能，为了访问不同包下的同名模块，需要加上：
#package1.p1  package2.p1

#包下还可以有子包，例如我们的package1下还可以有package11，这个package11可以是和模块p1平级的
#一个文件夹要成为一个包，文件夹下必须有一个特定的文件：__init__.py，否则python就不会发现它
#init文件本身也是一个模块，可以再里面什么都不写，也可以和普通模块一样，写一些代码
#特别的，这个init文件的模块名就是它的包名：packages，而不像其他模块一样，例如packages.package1
# 假设我们在c7.py中定义了a=2，我们在其他地方也需要使用这个变量。这是软件复用的原理。
# 在packages中，如果要使用这个变量
#print(a)
#会提示没有引入，引入的语法有两个：
#import后只能跟模块名（packages.c7)
#import c7
#使用c7下的a，使用c7.a
#print(c7.a)

#python是一个解释性语言，执行时必须遵守先后次序，如果import在print后，解释器就不知道a是什么
#如果是编译型语言，因为会完成编译后再运行，有时候就可以先使用后定义。

#packages下自动生成了__pychache__这样一个目录，这是python解释器自动生成的文件夹，里面有一个二进制文件，
#这是一个pyc字节码文件，可以提升python程序的运行效率。

#python导入的第二种方式：
# from-import语句来导入具体的变量或者函数
# from c7 import a
#这里因为直接把变量引入进来了，所以访问a时不需要再加模块名
# print(a)
#也可以使用from import来引入整个模块
# from t import tc7
# print(tc7.a)

#通过from import * 可以导入某模块全部变量
#可以通过在被导入模块中加入__all__，来限制能被加入的变量名
# from t.tc7 import *
# print(a)

#很多时候，我们的多个模块可能都需要导入大量的系统类库，有一个简单的办法：
# 我们设置一个需要引入的公共包，在该包的__init__.py文件中，导入公用的系统类库，
# 然后在我们导入这个公共包时，__init__.py就会自动执行，自动引入了那些系统类库
<<<<<<< HEAD
import t
print(t.sys.path)

#注意：和C++不同，python的包和模块是不会重复导入的
#在一个文件中已经导入过的，就不会再重复导入，但是我们要避免循环导入：
# 例如，在这里我们写 from c7 import a 在c7中又写from package import a
# 就会导致循环引入

#导入一个模块时，就会执行一个模块中的全部代码
=======

#import t
#print(t.sys.path)
>>>>>>> addclass
