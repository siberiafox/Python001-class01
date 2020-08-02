学习笔记

一、Django 开发环境安装

安装

pip install django==2.2.13 

升级到此版本

pip install --upgrade django==2.2.13 

二、创建项目

1、django-admin startproject MyDjango

其中MyDjango是 自定义的项目名称

三、创建应用app

1、cd MyDjango

进入项目根文件下

2、python manage.py startapp index

创建应用，其中index 是自定义的应用名称

三、启动和停止Django应用程序

启动两种方式

1、python manage.py  runserver 

默认是127.0.0.1:8000

2、python manage.py  runserver 0.0.0.0:80

停止

CONTROL-C

四、settings.py

至少需要修改两个地方

INSTALLED_APPS：添加自己的app

DATABASES：自己的数据库


五、自己的工作特点是都是先创建了数据库表了，重点掌握通过表生成models

1、必须先配置好数据库信息

2、执行命令：

python manage.py inspectdb

python manage.py inspectdb > models.py


六、bootstrap框架

1、css

bootstrap.min.css

2、js

1、bootstrap.min.js

2、jquery.js


作业结果

执行python manage.py  runserver 0.0.0.0:80

访问：

http://localhost/movies

http://localhost/douban

