## python实操经验

#### 在print中使用赋值表达式

```python
i=1
j=0
while i<=100:
    print(j+=i)
    i+=1
```

程序报错：在 Python 中，使用 `+=` 等运算符的同时打印是不被支持的。你应该先计算赋值，然后再打印。此外，在 `print()` 函数中直接使用赋值表达式也是不合法的。

以下是修正后的代码：

```python
i = 1
j = 0
while i <= 100:
    j += i
    print(j)
    i += 1

```

#### while循环嵌套，内循环没有重置变量

```python
i=1
j=1
while i<=9:
    while j<=9:
        print(f"{i}*{j}={i*j}")
        j+=1
    i+=1
```

内层的 `while` 循环只会执行一次。你需要在外层循环开始的时候将 `j` 重置为 1，这样每次进入内层循环时 `j` 都会从 1 开始。

以下是修正后的代码：

```python
i = 1

while i <= 9:
    j = 1  # 重置 j 为 1
    while j <= 9:
        print(f"{i}*{j}={i*j}", end="\t")  # 使用制表符分隔每个结果
        j += 1
    print()  # 在一行的乘法表输出完之后换行
    i += 1
```

