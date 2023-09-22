# python学习

### 数据类型

#### 基本类型

- 字符串类型
- 整型（有符号）
- 浮点型（有符号）

##### 查看数据类型

`type()`会返回数据的类型

```python
print(type("hello world"))
int_data=520
print(type(int_data))
float_data=13.14
float_type=type(float_data)
print(float_type)

"""
输出
<class "str">
<class "int">
<class "float">
"""
```

##### 类型转换

`float(),int(),str()`改变数据类型

```python
int_data=int("11")
print(type(int_data),int_data)
```

**注意点**

不是所有字符串都能转整型、浮点型，如果字符串不全是数字执行时会报错

整型转浮点型会带上小数部分，例如`11`转成`11.0`

浮点型转整型会丢失小数部分，例如`11.353`转成`11`

#### 标识符(变量名)

**命名规则**

- 英文
- 中文(不推荐使用中文)
- 数字(不可以用在开头)
- 下划线(_)

这四类元素

**标识符区分大小写**

**不可使用关键字(保留字)**

#### 运算符

##### 算术运算符

- `+`加
- `-`减
- `*`乘
- `/`除
- `//`整除运算符`9//2=4`
- `%`取余运算符`9%2=1`
- `**`指数运算符`2**3=8`

##### 赋值运算符

- `=`把右边的数据赋值给左边的变量
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- `//=`
- `**=`幂赋值运算符,`a**=c`相当于`a=a**c`

#### 字符串

##### 字符串的三种定义方式

- 单引号`str='str1'`

- 双引号`str="str2"`

- 三引号`str="""str3"""`三引号支持多行数据

如果字符串本身包含引号可以，使用其他的引号定义，也可以使用转义符**(\\)**来解除引号的作用

##### 字符串拼接

使用**+**来进行字符串拼接

注意和**js**不同的是：字符串不能直接通过**+**来和整型或者浮点型进行拼接，否则会报类型错误

我们可以使用**字符串格式化**来进行字符串类型和整型的拼接

##### 字符串格式化

使用**%**进行占位

使用**s**表示将数据变成字符串放到占位的地方

```python
tel=15151226564
money=20.365
print("我的电话号码是%s,我的钱包余额是%s"%(tel,money))
#输出:我的电话号码是15151226564,我的钱包余额是20.365
```

多个变量拼接使用括号括起来，用逗号分隔，按照输入顺序填入占位的地方

`%s`字符串占位

`%d`整型占位

`%f`浮点型占位

##### 字符串格式化：数字精度控制

- `m`控制字符串宽度，设置的宽度小于数字本身**不生效**
- `.n`控制小数点精度，要求是数字，会进行**四舍五入**

`%5d`设置宽度为5，宽度不足会在前面补上**空格**

`%.2`设置小数点精度为2

`%5.2f`设置宽度为5，小数点精度为2，小数部分也计入宽度

##### 字符串格式化：快速写法

不理会类型，不做精度控制

```py
name="张三"
age=18
print(f"我的名字是{name},我的年龄是{age}")
```

类似**js**的模板字符串

##### 字符串格式化：表达式格式化

**表达式**是指有明确执行结果的代码语句

```python
str="hello world"
print("str的数据类型是%s"%(type(str)))
```

#### Input和print

print是输出

input是输入

##### input

input输入完成后使用回车键完成输入

input需要使用一个变量接收输入的值`str=input()`

input可以接收一个参数，进行输入提示

input接收输入的数据会变成字符串类型

```python
str=input("验证input获取到的数据类型?\n")
print(f"数据类型是{type(str)}")
#输出：数据类型是<class 'str'>
```

##### print

`print()` 函数有一个名为 `end` 的可选参数，它决定了在输出内容后要添加什么字符作为结尾，默认情况下是换行符 `\n`

**end参数**

```python
print("hello",end="")

print("world",end="")
```

#### 判断语句

##### 布尔类型

进行判断只有两个结果**真**或**假**

`True`表示真，`False`表示假

`True`本质上是数字记作**1**，`False`记作**0**

`print(3+True)`输出4

`print(3+True-False)`输出4

##### 比较运算符

- `>`
- `<`
- `==`
- `!=`
- `>=`
- `<=`

##### if判断语句

if 判断条件 :

[空格]条件成立的执行语句

**python中使用空格来确定语句归属，需要4个空格，一个tab就是4个空格 **

```python
if 10>5:
    print("10确实大于5")
```

**else**

`else`和`if`同级，`else`是判断语句的一个分支，用来兜底，当其他分支不执行时，执行`else`

**elif**

`elif`和`else`和`if`同级，`elif`是判断语句的一个分支

#### 循环语句

##### while循环语句

```python
i=0
while i<100:
    print("hello world %d"%i)
    i+=1
```

`while`后面的是循环条件，`while`条件需要得到布尔类型，`True`是继续循环，`False`是停止循环

一定要**设置循环终止条件**，否则会**无限循环**

**缩进**的要求同`if判断语句`

##### while循环嵌套

**一定要注意重置内循环的状态，否则内循环只循环一次！！！**

##### for循环

`while`本质上更像循环

`for`本质上更像遍历和迭代

`while` 循环像是一个开放式的“如果……那么”语句，只要条件为真，就会重复执行。而 `for` 循环像是一个计数的机制，用于遍历一系列元素

```python
for x in "hello world":
    print(x)
```

将hello world的字符串遍历，并赋予x临时变量

理论上for循环不可能无限循环，因为`in`的数据处理集不可能无限大

```python
str="skdfkshkhkhfsadhkas"
i=0
for x in str :
    if(x=="s"):
        i+=1
print("s一共出现了%d次"%i)
```

**for循环的变量作用域**

临时变量在编程规范上，只限度在`for`内部

如果在`for`外部访问临时变量是可以访问的

在编程规范上不建议这么做

```python
for i in range(5):
    print(i)
print(i)
#最后的i输出4
```

##### countine关键字

终止本次循环，直接进入下一次循环

在`for`和`while`中有同样的作用

在嵌套中使用，只对**当前循环**生效

##### break关键字

直接结束循环

在`for`和`while`中有同样的作用

在嵌套中使用，只对**当前循环**生效，记住他只是结束了当前循环，不是把当前循环代码删了

#### 函数

提高代码复用性和开发效率

##### 函数的定义

```python
def 函数名(参数):
    函数体
    return 返回值
```

##### 函数的调用

```python
函数名(参数)
```

函数必须**先定义**，再使用

##### return返回值

返回值也是函数执行的结果，可以用来赋值

不设置返回值返回**None**

`None`是一个特殊的字面量，类型为`NoneType`

- 一般用于if判断语句中，代表`False`
- 也可以给一个变量赋值为`None`意为暂时没有具体值

##### return多个返回值

```python
def myreturn():
    return 1,True,"hello"
x,y,z=myreturn()
```

##### 函数的多种参数

- 位置参数：根据函数的形参位置顺序，依次传递参数，**顺序个数必须一致**
- 关键字传参：函数调用时，在`()`里使用key(形参名)=value(实参)的方式进行传参，取消了参数传递的顺序要求，可以和位置参数混用
- 缺省参数：在函数定义时定义了参数的默认值，调用时不传该参数就使用默认值，无论定义还是调用，位置参数要在默认参数之前
- 不定长参数：不确定调用时会传入多少个参数（不传参也可以），分为位置不定长和关键字不定长两种

```python
#位置不定长
def mytest(*args):
    print(args)
mytest("hello")
mytest("hello","world",996)
#会把接收到的参数变成一个元组

#关键字不定长
def mytest(**kargs):
    print(kargs)
mytest(word1="hello")
mytest(word1="hello",Word2="world",num=996)
#会把接收到的参数变成一个字典
```

##### 匿名函数

**匿名函数的定义**

`lambda`关键字，可以定义**匿名函数**(无名称)

**有名称**的函数(使用`def`定义的)，可以基于函数名**无限次使用**

使用`lambda`定义的**匿名函数**只可以**临时使用一次**

**定义**

`lambda 参数:函数体(只能写一行代码，无法写多行)`

```python
def myprint(compute):
    print(compute(1,2))

myprint(lambda x,y:x+y)
#不用写return，直接就return了
```

前端OS：只能写一行，那我为啥不直接写表达式

##### 函数作为参数传递

前端OS：这可以当做特性来显摆吗？我一直以为所有语言都能这么玩

```python
def myprint(compute):
    print(compute(1,2))

def compute(a,b):
    return a+b
```

与**普通传参**不同，普通传参**传的是数据**，把**函数**作为参数传递，**传递的是逻辑**				

##### 函数的嵌套调用

```python
def b():
    print(2)
    print(3)
def a():
    print(1)
    b()
    print(4)
a()
```

在函数a中嵌套调用b，当a中的代码执行到b的时候，会在执行完b的所有代码后，再去执行a剩下的代码

#### 变量作用域

**全局作用域**和**局部作用域**两种

##### 局部变量

**局部变量**是在函数体**内部**的变量

```python
def a():
    num=15
    print(num)
a()
print(num) #报错num未定义
```

变量num的定义是在a函数内部，在外部访问报错

##### 全局变量

在函数**体内**，**体外**都能访问到的变量

如果非要在函数内部定义一个全局变量，可以使用global关键字

```python
def a():
    global num=15
    print(num)
a()
print(num) #15
```

### 数据容器

根据特点不同

- 是否允许元素重复
- 是否可以修改
- 是否有序

等，可以分为5类列表`list`、元组`tuple`、字符串`str`、集合`set`、字典`dict`

#### 列表List

前端OS:中括号，能用索引下标取，是数组！！！

##### 字面量

`[元素1，元素2，元素3，元素4]`

##### 定义变量

`变量名称=[元素1，元素2，元素3，元素4]`

##### 定义空列表

```python
变量名称=[]
变量名称=list()
```

##### 数据类型

使用`type`输出类型，结果为`<class 'list'>`

##### 下标索引

长度为n的列表

正向第一个元素下标是`0`，最后一个元素下标是`n-1`

反向第一个元素下标是`-1`，最后一个元素(也就是第一个元素)，索引值是`-n`

**下标索引取值**

```python
myList=["hello",69,13.14,[36,"world"]]
print(myList[-2])   #13.14
print(myList[0])    #"hello"
print(myList[3][1]) #world
```

##### 列表操作

**查找元素**

`列表.index(目标元素)`index会返回**目标元素**的下标

如果查找的元素不存在会**报错**

前端OS:`js`的`index`如果元素不存在会返回`-1`，但是python中`-1`也是索引，指的是最后一个元素

**插入元素**

`列表.insert(插入位置,要插入的元素)`例如`myList.insert(1,"python")`

在索引值为1的地方插入'python'，本来在索引值为1的元素会**往后移动**

​	**如果插入的位置索引超出列表的长度会报错**

**追加元素**

- 单个元素

​		`列表.append(目标元素)`将**目标元素**添加到列表尾部

- 多个元素

​		`列表.extend(其他元素容器)`将**其他元素容器**的内容取出，依次添加到列表尾部

​		`[0,1,2].extend([3,4,5])`会把`[0,1,2]`这个数组变成`[0,1,2,3,4,5]`

**删除元素**

- `del`关键字

​		`del 目标列表[索引]`

- `pop`方法

​		`目标列表.pop(索引)`

​		实际上是取出列表中的某个元素，这个方法的返回值是被取出的元素

**清空列表**

`列表.clear()`例如`myList.clear()`

**修改元素**

- 修改特定位置的元素(重新赋值)

​		`列表[索引]=要修改的值`例如`myList[2]="python"`

- 删除某个元素在列表中的**第一个匹配项**

​		`列表.remove(元素)`例如`myList[2]="python"`

**统计元素个数**

`列表.count(目标元素)`统计**目标元素**在列表中的个数

**列表长度**

`len(列表)`统计列表中的元素个数

![image-20230828000709418](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230828000709418.png)

#### 元组Tuple

一个只读的list，可以储存多种类型的数据，修改其中的元素会报错，但列表作为元组的一个元素，列表内部的值是可以改变的

前端OS:一个不能操作的数组，尤其是作为元组元素的列表内部的值是可以改变的，简直像是const arr=[[1,2,3],4,5,"hello"]

##### 字面量

`(元素1，元素2，元素3，元素4)`

##### 定义变量

`变量名称=(元素1，元素2，元素3，元素4)`

##### 定义空元组

```python
变量名称=()
变量名称=tuple()
```

##### 数据类型

使用`type`输出类型，结果为`<class 'tuple'>`

##### 下标索引

**同`list`**

##### 元组操作

只支持**`index`,`len()`,`count()`**，且使用方法**同`list`**

![image-20230828002848175](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230828002848175.png)

#### 字符串String

前端OS：这就是字符串，嗯

##### 定义变量

`str="hello world"`

##### 下标索引

可以使用下标索引取值，`js`中也可以，但我很少去用

##### 字符串操作

![image-20230831215523354](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230831215523354.png)

#### 序列

**序列支持切片**

**列表，元组，字符串，均支持切片操作**

**语法:`序列[开始位置:结束位置:步长]`**

可以**参数不传**，默认值开始位置为**数据容器起点**，结束位置为**数据容器终点**，步长默认为**1**

切片的起始位置默认为 0，即第一个元素的索引为 0。切片操作**包括起点**，但**不包括终点**

#### 集合set

**`列表`**支持**修改**，支持**重复元素**，**有序**

**`字符串`**，**`元组`** **不支持修改**，支持**重复元素**，**有序**

**`集合`**最大的特点，**不支持重复元素**，**无序**(无序就说明，不支持下标索引访问)，允许**修改**

前端OS：出现了！集合！！！

##### 定义集合


```python
test={"string","list","tuple","set","string","set"}
#输出test
#{"string","list","tuple","set"}
```

定义时元素可以重复

输出时自动去重

##### 集合操作

##### 集合遍历

因为**不支持下标索引**所以**不能使用while遍历**

但可以使用**for遍历**

![image-20230831223236393](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230831223236393.png)

#### 字典

不支持下标索引，**无序**，**key不可重复**

使用花括号`{}`，储存键值对`key:value`

前端OS：我觉得是js里最好用的数据容器了

##### 定义字典

```python
dict1={}
dict2=dict()
dict3={"周杰伦":100,"扁嘴伦":102,"郭艾伦":98}
```

**不允许key重复**，同名的key，后面的会**覆盖**前面的

##### 字典取值

`number=dict3["扁嘴伦"]`

##### 字典嵌套

字典可以作为字典某一个key的value，来实现字典的**嵌套**

**字典可嵌套，取值可叠加**

字典的键（key）可以是以下数据类型：

不可变数据类型：

- 字符串（string）
- 数字（integer、float、complex）
- 布尔值（boolean）
- 元组（tuple）

内置的哈希类型：

- 字节串（bytes）

字典的键必须是**不可变的**，因为字典使用**哈希表**来实现快速查找和访问。可变的数据类型（如列表）不能用作字典的键，因为它们的哈希值可以发生变化，从而破坏了字典的内部结构。

##### 字典操作

![image-20230831225922087](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230831225922087.png)

#### 数据容器对比

|          | 列表               | 元组                 | 字符串     | 集合           | 字典                       |
| -------- | ------------------ | -------------------- | ---------- | -------------- | -------------------------- |
| 元素数量 | 多个               | 多个                 | 多个       | 多个           | 多个                       |
| 元素类型 | 任意               | 任意                 | 字符       | 任意           | 键值对                     |
| 重复元素 | 支持               | 支持                 | 支持       | 不支持         | 不支持                     |
| 下标索引 | 支持               | 支持                 | 支持       | 不支持         | 不支持                     |
| 是否只读 | 否                 | 只读                 | 只读       | 否             | 否                         |
| 使用场景 | 可修改可重复的数据 | 不可修改可重复的数据 | 一串字符串 | 不可重复的数据 | 以key检索value，有对应关系 |

##### 数据容器通用操作

多数数据容器都支持下标索引取值，所以多数数据容器都支持`while`遍历

数据容器都支持`for`遍历

数据容器的通用方法`len()`,`min()`,`max()`

数据容器间可以**互相转化**，注意**字典**和**字符串**在转换成**其他数据容器**时会**有变化**，例如字典转换成列表就只剩`key`，而丢掉了`value`

**`sorted(数据容器,[reverse=True])`**第二个参数默认为`False`

将数据容器排序按**`从小到大`**的顺序排序，如果第二个参数传`True`则**`从大到小`**排序，然后放进**列表**里,你懂的，看上面↑

字母的大小取决于他的`ascii`值

![image-20230831232707221](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230831232707221.png)



#### 文件操作

##### 操作文件的步骤

- 打开

- 读写
- 关闭

##### open()打开函数

`open(name，mode，encoding)`

三个**常用参数**，**encodeing**其实是**第四个**参数，所以我们用**关键字传参**，而不是位置传参

`f=open("D:/测试.txt","r",encoding="UTF-8")`

​	**name**要打开的目标文件名的字符串(可以包含目标文件的具体路径)

​	**mode**设置文件的访问模式(**只读**，**写入**，**追加**)

​	**encoding**编码格式，推荐使用**UTF-8**

**mode**常用的三种访问模式

![image-20230901220551881](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230901220551881.png)

##### 读操作的相关方法

- **文件对象.read(num)**

读取文件内容，**num**为读取文件的字节数，不传入**num**则读取所有数据

- **文件对象.readlines()方法**

readlines可以按照**行**的方式，把**整个文件内容**一次性读取，返回一个**列表**，**每一行数据为一个元素**

- **文件对象.readline()方法**

readlines可以按照**行**的方式，**一行一行**的读取文件内容

------

在程序中连续调用两次`read`，第一次读取的结尾会被记录下来

第二次调用`read`的时候，会从**第一次的结尾**继续读

在**读文件**的时候，只要文件打开，不管调用什么方法，文件都会从**上一次读的结束位置继续开始**

------

可以使用for一行一行的遍历文件内容

```python
for line in open("python.txt","r"):
    print(line)
```

##### close()关闭函数

```python
f=open("python.txt","r")
f.close()
```

通过close关闭文件，如果不使用close关闭文件，并且**不结束程序**，那么python会一直**占用该文件**

##### with open语法

```python
with open ("python.txt","r") as f:
    f.read()
```

通过**with open**操作文件，可以在操作完成后**自动调用close**进行关闭

##### 基本写操作

```python
f=open("python.txt","w")
#打开文件
f.write("hello world")
#将内容写入内存中
f.flush()
#将内存中的内容刷到硬盘上
```

**write**并**没有完成文件写入**的操作，只是**将内容暂时存到内存中**，等**flush**执行时将**内存**中的内容**统一写入**硬盘

这样的好处是**不需要频繁操作硬盘导致效率下降**

前端OS：这让我想到vue框架，收集dom操作，最后统一渲染到页面上去，这样就提高了效率和资源损耗，也让我想到了使用canvas画				板，在画完东西之后，需要执行stroke()才能真正画出东西

##### 基本追加操作

不会像w一样覆盖原有内容，而是在原有内容后面接着写

```python
f=open("python.txt","a")
#打开文件
f.write("hello world")
#将内容写入内存中
f.flush()
#将内存中的内容刷到硬盘上
```

**write**并**没有完成文件写入**的操作，只是**将内容暂时存到内存中**，等**flush**执行时将**内存**中的内容**统一写入**硬盘

#### 异常

这还用我解释？

**遇到bug的两种处理方式**

- 不去理会，程序崩溃终止运行
- 对bug进行处理，程序继续运行

##### 捕获异常

- 捕获常规异常

```python
try:
    可能出现异常的代码
except:
    出现异常的操作
```

- 捕获指定类型异常

```python
try:
    可能出现异常的代码
except NameError as e:
    print("出现了变量未定义的异常")
```

- 捕获多个异常

```python
try:
    可能出现异常的代码
except (NameError,ZeroDivisionError):
    print("出现了变量未定义异常 或者 出现了除零异常")
```

- 捕获所有异常

```python
try:
    可能出现异常的代码
except Exception as e:
    print("出现了异常")
    print(e)
    
#或者

try:
    可能出现异常的代码
except:
    出现异常的操作
```

##### 异常的else和finally语法

```python
try:
    可能出现异常的代码
except:
    异常处理
else:
    没出现异常的情况
finally:
    无论是否出现异常都会执行
```

前端OS：这finally好像promise的finally啊

##### 异常的传递性

当函数func01中发生异常，并且没有捕获处理这个异常的时候，异常会传递到函数func02，当func02也没有捕获处理这个异常的时候main函数会捕获这个异常，这就是异常的传递性

前端OS：连续使用promise，可以在最后使用catch统一捕获错误

![image-20230901235313885](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230901235313885.png)

#### 模块Module

前端OS：没必要解释，懂的都懂

##### 模块的导入

**`[from 模块名] import [模块|类|变量|函数|*] [as 别名]`**

`from`和`as`可以不写

##### 自定义模块

```python
#test.py
def plus(a,b):
    return a+b
```

```python
#当前文件
import test
test.plus(1,2)
```

自定义模块的模块名，就是py文件名

引入同名的模块，类，变量，函数，后面引入的会覆盖前面引入的

##### \_\_mian\_\_

只有在自己原本的文件中`__name__=="__mian__"`，这样可以在自定义模块中测试，又不用担心在引入模块时函数就调用

```python
def plus(a,b):
    return a+b
if __name__=="__mian__":
    plus(1,2)
```

##### \_\_all\_\_

```python
#test.py
__all__=['test_A']

def test_A(a,b):
    return a-b
def test_B(a,b):
    return a+b
```

```python
from test import *
#这里使用*
#如果没有写__all__，那么引入所有内容
#如果写了__all__，那么只引入__all__中准备的内容
```

##### 自定义包

只有文件夹里有**\_\_init\_\_.py**文件，才被称之为**包**

\_\_init\_\_.py文件可以**没有内容**，但**必须存在**

\_\_init\_\_.py文件里会写\_\_all\_\_的配置

##### 第三方包安装

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称`

在**pip**中使用清华大学提供的镜像下载第三方包

#### JSON

JSON数据格式用于在各种编程语言之间传递数据

前端OS：我可太熟悉了，我说怎么字典第一眼看上去这么眼熟，原来就是JSON

`JSON`和`python`中的**字典**，**列表嵌套字典**可以无缝切换，不能说相似吧，只能说是一模一样

##### JSON数据转化

将JSON数据与python数据之间互相转化

前端OS：是不是`JSON.stringfly`和`JSON.parse`啊？

- 引入JSON库

`import json`

- python数据转化成JSON数据

```python
data=[{"name":"张三","age":18},{"name":"李四","age":19}]

data=json.dumps(data)
#将python数据转为JSON字符串

data=json.loads(data)
#将JSON字符串转为python数据
```

中文转换时会有编码问题，我们可以设置**`ensure_ascii=False`**

```python
import json

data=[{"name":"张三","age":18},{"name":"李四","age":19}]

data=json.dumps(data,ensure_ascii=False)
#将python转为JSON
#设置ensure_ascii=False的意思是不使用ascii来转换他，把内容直接输出出去
#如果不设置，那么中文就会变成unicode字符
```

### 数据组织

- 设计表格(创建类)

- 打印表格(类实例化成对象)

- 填写表格(在对象中填写数据)

```python
#创建类
class Student:
    name=None
    grade=None
    age=None
    score=None
#类实例化成对象   
student1=Student()
#在对象中填写数据
student1.name="张三"
student1.grade=5
student1.age=14
student1.score=100
```

#### 类的定义与使用

##### 定义类

```python
class 类名:
    类的属性，定义在类中的变量（成员变量）
    类的方法，定义在类中的函数（成员方法）
    
#类中定义方法必须传一个self参数，你在调用方法的时候可以当他不存在
#通过self可以获取类内部的成员变量
class Student:
    name=None
    grade=None
    def say_hi(self):
        print(f"你好，我是{self.name}")
    def say_words(self,words):
        print(words)
student1=Student()
student1.say_words("今晚吃什么？")
```

##### 创建对象 

`变量名=类名()`

##### 构造方法

在python类中可以使用构造方法\_\_init\_\_

\_\_init\_\_方法会在创建类，构造类对象时自动执行

在创建类，构造类对象时，会将传入的参数自动传递给\_\_init\_\_使用

```python
class Clock:
    price = None
    id = None
    def __init__(self,price,id):
        self.price=price
        self.id=id
    def ring(self):
        winsound.Beep(2000, 3000)

clock1 = Clock(998,"001")
```

##### 魔术方法

- \_\_str\_\_  **转字符串方法(重写object方法)**
```python
class Clock:
    price = None
    id = None
    def __init__(self,price,id):
        self.price=price
        self.id=id
    def ring(self):
        winsound.Beep(2000, 3000)
    def __str__(self):
        return f"闹钟{self.id}价格{self.price}"
    
print(clock1)
print(str(clock1))
#闹钟001价格998
#闹钟001价格998
```

- \_\_lt\_\_  **小于比较符号方法**
用于两个对象之间直接比较大小，支持**小于**和**大于**
```python
class Clock:
    price = None
    id = None
    def __init__(self,price,id):
        self.price=price
        self.id=id
    def ring(self):
        winsound.Beep(2000, 3000)
    def __lt__(self, other):
        return self.price < other.price

clock1 = Clock(998,"001")
clock2 = Clock(360,"002")
print(clock1>clock2)
#True
```

- \_\_le\_\_  **小于等于比较符号方法**
用于两个对象之间直接比较大小，支持**小于等于**和**大于等于**
```python
class Clock:
    price = None
    id = None
    def __init__(self,price,id):
        self.price=price
        self.id=id
    def ring(self):
        winsound.Beep(2000, 3000)
    def __le__(self, other):
        return self.price <= other.price

clock1 = Clock(998,"001")
clock2 = Clock(360,"002")
print(clock1>=clock2)
#True
```

- \_\_eq\_\_  **等于比较符号方法**
懒得写了



#### 封装

###### 私有成员

- 通过使用`__`来开头定义私有变量

- 通过使用`__`来开头定义私有方法

只要在类中设置了私有成员，我们在获取的**类对象**中，就无法使用这些变量或方法

私有成员，类对象不可以使用，但是类中的其他成员可以使用



#### 继承

- 继承语法

```python
class 类名(父类名):
    类内容体
```

- 多继承

```python
class 类名(父类名1,父类名2,父类名3):
    类内容体
```
如果继承来的父类中的成员名有重名，谁先来的，谁的优先级更高

- `pass`关键字

```python
class 类名(父类名1,父类名2,父类名3):
    pass
	//只继承父类的成员，不再额外添加新内容，用于补全语法
```

##### 复写

在**子类**的类内容体中**重写**继承来的**父类中的同名的成员变量或方法**

##### 调用被复写的父类中的同名的成员

一旦在子类中复写，类对象调用成员时，就会调用复写的新成员

如果需要重新调用被复写的父类中的成员，需要使用以下方法

- 调用父类成员

使用成员变量：**父类.成员变量**

使用成员方法：**父类.成员方法(self)**

- 使用super()调用父类成员

使用成员变量：**super().成员变量**

使用成员方法：**super().成员方法()**

#### 注解

前端OS：死去的TypeScript突然开始攻击我

- 对变量进行注解

```python
简单注解
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_set:set={1,2,3}
my_dict:dict={"age":18}
my_str:str="hello world"

my_list=[1,2,3]			#type: int
my_tuple=(1,2,3)		#type: int
my_set={1,2,3}			#type: int
my_dict={"age":18}		#type: dict[str,int]
my_str="hello world"	#type: str

复杂注解
my_list:list[int]=[1,2,3]
my_tuple:tuple[int,str,bool]=(1,"hello",True)
my_set:set[int]={1,2,3}
my_dict:dict[str,int]={"age":18}
my_str:str="hello world"

my_list=[1,2,3]					#type: list[int]
my_tuple=(1,"hello",True)		#type: tuple[int,str,bool]
my_set={1,2,3}					#type: set[int]
my_dict={"age":18}				#type: dict[str,int]
my_str:str="hello world"
```

- 对方法的形参列表和返回值进行注解

前端OS：什么TypePython

```python
def 函数名(形参名:类型) -> 返回值类型:
    pass

def my_function(a:int,b:int) -> int:
    return a+b
```

#### Union类型

前端OS：感觉不如 `name:string|null`

```python
from typing from Union

my_list:list[Union[int,bool,str]]=[1,2,3,False,"hello"]

my_dict:dict[str,Union[int,str]]={"name":"jack","age":18}

def my_function(data:Union[int,str]) -> Union[int,str]:
    return data
```

#### 多态

同样的行为(方法)，传入不同的对象，得到不同的结果

多态常用在继承关系上

##### 抽象类(接口)

**定义**

**抽象类**指含有抽象方法的类

**抽象方法**指方法体是**空实现**的方法

**设计含义**

父类**只确定有哪些方法**，但**不去指定方法中的内容**，而是使用`pass`把**方法体置为空**，让**继承父类的子类去确定方法的内容**

配合**多态**，完成**抽象的父类设计**，**具体的子类实现**



#### range语句

注意range只是生成一个可迭代对象，不是去生成一个list的方法

`print(type(range(10)))`输出`<class 'range'>`

range(num)

形成一个0到num的数字序列，不包含num

range(num1,num2)

形成一个num1到num2的数字序列，包含num1，不包含num2

range(num1,num2,step)

形成一个num1到num2的数字序列，步长为step，包含num1，不包含num2

`range(5,10,1)`输出`[5,7,9]`



#### random

引入random

`import random`

使用random的方法

```10python
num=random.randint(1,100)
```

生成一个1，100之间的整型数据，不包含100，也就是1-99







