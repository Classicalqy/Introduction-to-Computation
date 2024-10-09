# -*- coding: utf-8 -*-

#%% 内置输入函数 input —— 行式输入

# 函数参数：一个字符串，用来给出合适的提示信息
# 函数返回值：一个字符串对象
#            其中，包含用户在 Enter 键之前的所有输入 
#            (但不包括输入时行末尾的换行符)

# 在使用输入信息之前，一般都需要根据实际需求进行类型转换

## 重要提示：在编程网格或者其它平台上做题时，
##          调用 input 函数不要使用任何提示字符串作为实参！！
##          要以无参的方式调用 input 函数，即 input()


#%% 例，输入一行字符型信息
name = input('Pls input your name:')
print(name)


#%% 例，输入一个整数 (一行里只输入一个整数)
intNum = int(input('Pls input an integer:'))
print(intNum)


#%% 例，输入一个浮点数 (一行里只输入一个浮点数)
fltNum = float(input('Pls input a floating number:'))
print(fltNum)


#%% 例，输入一个整数和一个浮点数 (两个数之间用空格分隔)
numbers = input('Pls input an integer and a floating number:')
nums = numbers.split()

print(nums)
print(int(nums[0]))
print(float(nums[1]))


# s.split() 的结果为一个表，其中的元素是
# 用连续空白字符 (空格/换行/制表符) 切分字符串 s 后所得到的一些子串
 


#%% 字符串的 split 方法示例，更多用法请查看手册

print(' 1  2  3  '.split())

print('1,2,3'.split(','))

print('1, 2, 3'.split(','))

print('1,2,,3'.split(','))



#%% 实例：输入三角形三边长，计算并输出面积

from math import sqrt

a = float(input("Length of edge a: "))
b = float(input("Length of edge b: "))
c = float(input("Length of edge c: "))
s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))
print("area =", area)

# 实现：
# 1) 简单的人机交互
# 2) 根据实际的输入数据，计算得到结果
# 3) 一个通用的、由三角形三边长算三角形面积的程序


#%% 一个简单的 Python 程序框架

# 1) 导入模块: 用 import 导入需要用到的模块
# 2) 获取数据：调用 input 函数从键盘输入 (或者从文件读入) 需要处理的数据
# 3) 计算与操作：按照设计好的计算过程，进行计算或者处理数据
#               其中，根据需求可能调用各种函数
# 4) 输出结果: 调用 print 函数将结果输出到屏幕 (或者写入文件)
