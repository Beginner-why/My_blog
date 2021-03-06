# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q
from blog.models import User
import re

class LoginForm(forms.Form):
    '''
    登录Form，只需要用户名和密码
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})

class RegForm(forms.Form):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "请输入您的用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "请输入您的邮箱", "required": "required",}),
                              max_length=50,error_messages={"required": "email不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "请输入您的站点", }),
                              max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "请输入您的密码", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})

class CommentForm(forms.Form):
    '''
    评论表单
    '''
    # 这里可以直接定义模板中的class等属性
    author = forms.CharField(widget=forms.TextInput(attrs={"id": "author", "class": "comment_input",
                                                           "required": "required","size": "25",
                                                           "placeholder": "用户名(必填)", "tabindex": "1"}),
                              max_length=50, error_messages={"required":"username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"id":"email","type":"email","class": "comment_input",
                                                           "required":"required","size":"25",
                                                            "placeholder": "邮箱(必填)", "tabindex":"2"}),
                                 max_length=50, error_messages={"required":"email不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"id":"url","type":"url","class": "comment_input",
                                                       "size":"25", "placeholder": "网址", "tabindex":"3"}),
                              max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"id":"comment","class": "message_input",
                                                           "required": "required", "cols": "25",
                                                           "placeholder": "请输入您的评论或留言(必填)",
                                                           "rows": "5", "tabindex": "4"}),
                                                    error_messages={"required":"评论不能为空",})
    article = forms.CharField(widget=forms.HiddenInput())



