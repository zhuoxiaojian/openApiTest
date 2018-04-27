# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:36
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from webuser.models import UserBase
class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = '__all__'