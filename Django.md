# Django学习

## 项目前期

### 项目
#### 项目创建



#### 项目文件结构


### APP
#### APP创建

#### APP文件结构



### 快速上手

### 项目启动

### 模板语法

### 网络请求

#### 请求与相应

```python
from django.shortcuts import render,HttpResponse,redirect
def test(request):
    #request.method请求的方式GET和POST
    print(request.method)
    #获取请求的query参数
    print(request.GET)
    #获取post请求的数据
    print(request.POST)
    
    #回应，返回字符串内容给请求者
    return HttpResponse("request")
	#回应，返回html内容给请求者
    return render(request,'test.html',{"name":"jack","age":18})
	#回应，将页面重定向到其他页面
    return redirect("www.baidu.com")
```

### 数据库操作

#### 数据库配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Django操作表

- 创建表

```python
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    age=models.IntegerField()
```

执行命令

```cmd
python manage.py makemigrations
python manage.py migrate
```

- 修改表中的列
新增一个列的时候，需要注意表格中已经有的数据，新增的列的值是什么

1. 手动输入一个值
2. 配置默认值
3. 允许为空
`age=models.IntegerField(null=True,blank=True)`

- 删除表

#### Django操作数据

- 新增数据
**`表名.objects.create(表项=数据)`**
- 删除数据
1.删除某些数据**`表名.objects.filter(id=3(筛选条件)).delete()`**
2.删除全部**`表名.objects.all().delete()`**


- 修改数据
1.修改某些数据**`表名.objects.filter(id=3(筛选条件)).update(表项=新数据)`**
2.修改全部数据**`表名.objects.all().update(表项=新数据)`**、


- 查询数据
1.查询某些数据**`表名.objects.filter(id=3(筛选条件))`**
2.查询全部数据**`表名.objects.all()`**这样获取到的是一个QuerySet类型数据，列表里是一个个对象
3.查询第一条数据**`表名.objects.filter(id=3(筛选条件)).first()`**这样获取到的是一个对象