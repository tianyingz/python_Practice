line = '----------------------------------------------------------------------------------------------\n'
print('第一题:实现100以内的数字之和')
print(sum(range(101)))
print(line)

print('第二题:在函数内修改全局变量')
a = 100
def update():
    global a
    a = 150
    return a
print(update())
print(line)

print('第三题:列出python3的标准库')
mode = {'1':'os,处理文件和文件夹',
        '2':'sys,命令行参数',
        '3':'re,字符串正则匹配',
        '4':'math,数学计算',
        '5':'datetime,处理日期时间',
        '6':'unit test, 单元测试模块',
        '7':'doctest,字符串测试',
        '8':'zlib,数据压缩',
        '9':'timeit,性能度量模块'}
print(mode)
print(line)

print('第四题:删除键和和并字典')
dict1 = {'1':'a','2':'b','3':'c'}
dict2 = {'4':'d','5':'e','6':'f'}
'删除键'
dict1.pop('1')
print(dict1)
'合并字典'
dict1.update(dict2)
print(dict1)
print(line)

print('第五题:GIL的使用')
print('GIL是python的全局解释器锁，在一个进程中有多个线程在运行时当前在运行的线程会占用整个python解释器（加了一把锁GIL）\n'
'使得进程内的其他线程无法运行，在当前运行的线程结束或遇到耗时操作时才会解开，运行其他线程。\n' 
'多进程程序在运行时给每个进程都分配了资源，相当于每个进程都有一个解释器，可以实现多线程同时运行；缺点是资源消耗大。')
print(line)

print('第六题:实现列表去重和列表合并')
test_list_1 = [1,1,2,2,3,3,4,4]
test_list_2 = [5,6,7]
'列表去重'
test_list_1 = set(test_list_1)
test_list_1 = list(test_list_1)
print(test_list_1)
'列表合并'
test_list_sum = test_list_1 + test_list_2
print(test_list_sum)
print(line)

print('第七题:python中的不定长参数')
print('一个*号表示传入的参数数量不固定(传入的参数是列表)，如下')
def change_number(*v):
    for i in v:
        print(i)
change_number('a','b','c')
print('两个*号表示传入的参数的长度不固定（传入的参数是键值对），如下')
def change_key(**key):
    for i,j in key.items():
        print(i,j)
change_key(name='tian')
print(line)

print('第八题:python2和python3的区别')
difference = {1:'print函数，python2中使用空格，python3使用括号',
              2:'range函数，python2中返回列表，python3返回迭代器',
              3:'input函数，python2中input输入的是int型，raw_input输入str（字符串），python3中input输入str',
              4:'字符串存储，python2中使用16位bit，unicode存储，python3中使用8位bit存储',
              5:'类的差别，python2中有新式类和老式类的区别，python3中统一使用新式类（统一继承object类）'}
print(difference)
print(line)

print('第九题:python3的数据类型')
python_type = {1:'int,整型',
               2:'str,字符串',
               3:'list,列表',
               4:'tuple,元组',
               5:'set,集合',
               6:'dict,字典',
               7:'bool,布尔型'}
print(python_type)
print(line)

print('第十题:面向对象中_new_和_int_的区别')
print('__new__在实例创建之前调用，是用来创建实例然后返回该实例（是一个静态方法）;__int__在new__之后被\n'
      '调用，用于设置对象属性的初始值(第一个值是__new__的实例\n'
      '可以参考:https://blog.csdn.net/jacsice/article/details/40349065')
print(line)

print('第十一题:一句话解释什么样的语言能够使用装饰器')
print('函数可以作为参数传递的语言可以使用装饰器')
print(line)

print('第十二题:简述with打开文件帮我们做了什么？')
print('执行了关闭文件的操作,可以参考:https://blog.csdn.net/dingo11/article/details/82880539')
print(line)

print('第十三题:列表[1,2,3,4,5]，请使用map函数输出[1,4,9,16,25]并使用列表推导式提取出大于10的数，最终输出[16,25]')
test_list_13 = [1,2,3,4,5]
def square(x):
    return x * x
test_list = list(map(square,test_list_13))
print(test_list)
test_list = [i for i in test_list if i > 10]
print(test_list)
print(line)

print('第十四题:生成随机整数、随机小数、0-1之间的小数')
import random
print('整数',random.randint(0,100))
print('随机小数',random.uniform(0,100))
print('指定小数精度',round(random.uniform(1,100),2)) #round是使用四舍五入来控制小数精度
print('0-1之间的小数',random.random())
print(line)

print('第十五题:字符串转义')
print('r,表示原始字符串，不进行转义')
print('u,将字符串的编码格式指定为unicode编码，主要对中文使用')
print('b,表示后面的字符串是byte类型')
print(line)

print('第十六题:使用re模块提取字符串')
import re
r = '''<li><a id="blog_nav_newpost" class="menu" rel="no000111follow">新随笔</a></li>'''
text = re.findall('''<a(.*?)</a>''',r)
print(text)
print(line)

print('第十七题:断言')
text = '这是一条测试数据'
assert('这' in text)
print('断言成功，失败会报错，程序中止')
print(line)

print('第十八题:连接数据库，执行一条sql语句')
import mysql.connector
'''mydb = mysql.connector.connect(
    host = '这里输入主机地址',
    port = '这里输入数据库端口号',
    user = '这里输入用户名',
    passwd = '这里输入密码'
)
mysql = mydb.cursor()
mysql.execute('这里选择数据库')
sql = '这里输入sql语句'
mysql.execute(sql)'''
print(line)

print('第十九题:10个Linux常用命令')
linux = {1:'cd,切换目录',
         2:'cp,复制文件',
         3:'rm,删除文件',
         4:'mkdir,创建文件夹',
         5:'ls,查看全部文件',
         6:'pwd,查看当前文件的绝对路径',
         7:'touch,修改文件的时间戳或是新建文件',
         8:'tree,查看目录结构',
         9:'cat,查看、修改文件内容，创建文件，也可以用来合并文件',
         10:'grep,搜索文件内容，所有用户可用的全局正则表达式搜索文本',
         11:'echo,打印文本，用于字符串输出'}
print(linux)
print(line)

print('第二十题:python中的数据类型')
Class = {1:'number,数字。属于不可变的数据类型',
         2:'str,字符串。属于不可变的数据类型',
         3:'tuple,元组。属于不可变的数据类型',
         4:'list,列表。属于可变对象',
         5:'dict,字典。属于可变对象',
         6:'set,集合。属于可变对象'}
print(Class)
print(line)

print('第二十一题:将ajldjlajfdljfddd去重，并按从大到小输出')
str = 'ajldjlajfdljfddd'
str = list(set(str))
str.sort()
print(str)
print(line)

print('第二十二题:使用匿名函数实现两个数相乘')
product = lambda x,y:x * y
print(product(2,3))
print(line)


line = '----------------------------------------------------------------------------------------------\n'
print('第一题:实现100以内的数字之和')
print(sum(range(101)))
print(line)

print('第二题:在函数内修改全局变量')
a = 100
def update():
    global a
    a = 150
    return a
print(update())
print(line)

print('第三题:列出python3的标准库')
mode = {'1':'os,处理文件和文件夹',
        '2':'sys,命令行参数',
        '3':'re,字符串正则匹配',
        '4':'math,数学计算',
        '5':'datetime,处理日期时间',
        '6':'unit test, 单元测试模块',
        '7':'doctest,字符串测试',
        '8':'zlib,数据压缩',
        '9':'timeit,性能度量模块'}
print(mode)
print(line)

print('第四题:删除键和和并字典')
dict1 = {'1':'a','2':'b','3':'c'}
dict2 = {'4':'d','5':'e','6':'f'}
'删除键'
dict1.pop('1')
print(dict1)
'合并字典'
dict1.update(dict2)
print(dict1)
print(line)

print('第五题:GIL的使用')
print('GIL是python的全局解释器锁，在一个进程中有多个线程在运行时当前在运行的线程会占用整个python解释器（加了一把锁GIL）\n'
'使得进程内的其他线程无法运行，在当前运行的线程结束或遇到耗时操作时才会解开，运行其他线程。\n' 
'多进程程序在运行时给每个进程都分配了资源，相当于每个进程都有一个解释器，可以实现多线程同时运行；缺点是资源消耗大。')
print(line)

print('第六题:实现列表去重和列表合并')
test_list_1 = [1,1,2,2,3,3,4,4]
test_list_2 = [5,6,7]
'列表去重'
test_list_1 = set(test_list_1)
test_list_1 = list(test_list_1)
print(test_list_1)
'列表合并'
test_list_sum = test_list_1 + test_list_2
print(test_list_sum)
print(line)

print('第七题:python中的不定长参数')
print('一个*号表示传入的参数数量不固定(传入的参数是列表)，如下')
def change_number(*v):
    for i in v:
        print(i)
change_number('a','b','c')
print('两个*号表示传入的参数的长度不固定（传入的参数是键值对），如下')
def change_key(**key):
    for i,j in key.items():
        print(i,j)
change_key(name='tian')
print(line)

print('第八题:python2和python3的区别')
difference = {1:'print函数，python2中使用空格，python3使用括号',
              2:'range函数，python2中返回列表，python3返回迭代器',
              3:'input函数，python2中input输入的是int型，raw_input输入str（字符串），python3中input输入str',
              4:'字符串存储，python2中使用16位bit，unicode存储，python3中使用8位bit存储',
              5:'类的差别，python2中有新式类和老式类的区别，python3中统一使用新式类（统一继承object类）'}
print(difference)
print(line)

print('第九题:python3的数据类型')
python_type = {1:'int,整型',
               2:'str,字符串',
               3:'list,列表',
               4:'tuple,元组',
               5:'set,集合',
               6:'dict,字典',
               7:'bool,布尔型'}
print(python_type)
print(line)

print('第十题:面向对象中_new_和_int_的区别')
print('__new__在实例创建之前调用，是用来创建实例然后返回该实例（是一个静态方法）;__int__在new__之后被\n'
      '调用，用于设置对象属性的初始值(第一个值是__new__的实例\n'
      '可以参考:https://blog.csdn.net/jacsice/article/details/40349065')
print(line)

print('第十一题:一句话解释什么样的语言能够使用装饰器')
print('函数可以作为参数传递的语言可以使用装饰器')
print(line)

print('第十二题:简述with打开文件帮我们做了什么？')
print('执行了关闭文件的操作,可以参考:https://blog.csdn.net/dingo11/article/details/82880539')
print(line)

print('第十三题:列表[1,2,3,4,5]，请使用map函数输出[1,4,9,16,25]并使用列表推导式提取出大于10的数，最终输出[16,25]')
test_list_13 = [1,2,3,4,5]
def square(x):
    return x * x
test_list = list(map(square,test_list_13))
print(test_list)
test_list = [i for i in test_list if i > 10]
print(test_list)
print(line)

print('第十四题:生成随机整数、随机小数、0-1之间的小数')
import random
print('整数',random.randint(0,100))
print('随机小数',random.uniform(0,100))
print('指定小数精度',round(random.uniform(1,100),2)) #round是使用四舍五入来控制小数精度
print('0-1之间的小数',random.random())
print(line)

print('第十五题:字符串转义')
print('r,表示原始字符串，不进行转义')
print('u,将字符串的编码格式指定为unicode编码，主要对中文使用')
print('b,表示后面的字符串是byte类型')
print(line)

print('第十六题:使用re模块提取字符串')
import re
r = '''<li><a id="blog_nav_newpost" class="menu" rel="no000111follow">新随笔</a></li>'''
text = re.findall('''<a(.*?)</a>''',r)
print(text)
print(line)

print('第十七题:断言')
text = '这是一条测试数据'
assert('这' in text)
print('断言成功，失败会报错，程序中止')
print(line)

print('第十八题:连接数据库，执行一条sql语句')
import mysql.connector
'''mydb = mysql.connector.connect(
    host = '这里输入主机地址',
    port = '这里输入数据库端口号',
    user = '这里输入用户名',
    passwd = '这里输入密码'
)
mysql = mydb.cursor()
mysql.execute('这里选择数据库')
sql = '这里输入sql语句'
mysql.execute(sql)'''
print(line)

print('第十九题:10个Linux常用命令')
linux = {1:'cd,切换目录',
         2:'cp,复制文件',
         3:'rm,删除文件',
         4:'mkdir,创建文件夹',
         5:'ls,查看全部文件',
         6:'pwd,查看当前文件的绝对路径',
         7:'touch,修改文件的时间戳或是新建文件',
         8:'tree,查看目录结构',
         9:'cat,查看、修改文件内容，创建文件，也可以用来合并文件',
         10:'grep,搜索文件内容，所有用户可用的全局正则表达式搜索文本',
         11:'echo,打印文本，用于字符串输出'}
print(linux)
print(line)

print('第二十题:python中的数据类型')
Class = {1:'number,数字。属于不可变的数据类型',
         2:'str,字符串。属于不可变的数据类型',
         3:'tuple,元组。属于不可变的数据类型',
         4:'list,列表。属于可变对象',
         5:'dict,字典。属于可变对象',
         6:'set,集合。属于可变对象'}
print(Class)
print(line)

print('第二十一题:将ajldjlajfdljfddd去重，并按从大到小输出')
str = 'ajldjlajfdljfddd'
str = list(set(str))
str.sort()
print(str)
print(line)

print('第二十二题:使用匿名函数实现两个数相乘')
product = lambda x,y:x * y
print(product(2,3))
print(line)

print('第二十三题:字典根据键从大到小排序')
test_dict = {1:'a',
             3:'b',
             2:'c'}
test_set = sorted(test_dict.items())
test_dict = dict(test_set)
print(test_dict)
print(line)
00000000000000000000000000000
11111111111111111111111
0000000000000000000000