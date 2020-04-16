# 博客                                                                                                                                   
基于Django开发的博客                                                                                                                     
博客地址：www.wfreeagle.com                                                                                                             
                                                                                                                                        
                                                                                                                                         
开发环境                                                                                                                                 
•开发工具:Pycharm

•开发环境为:
Windows10
Python3.7.2
Django1.10.2
•数据库：Mysql5.7


安装项目所需依赖包

pip install django==1.10.2
pip install pymysql==0.8.0
pip install django-tinymce==2.8.0
pip install six==1.12.0
pip install pillow==6.2.1

连接mysql数据库

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'blogdb',  # 数据库名
    'USER': 'root',  # 用户名
    'PASSWORD': '',  # 密码
    'HOST': '',  # 主机IP
    'PORT': '',  # 端口
  }
}




