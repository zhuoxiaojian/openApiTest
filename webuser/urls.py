# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:42
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : urls.py
# @Software: PyCharm
from rest_framework import routers
from django.conf.urls import url, include
from .views import UserBaseViewSet, schema_view
router = routers.DefaultRouter()
router.register(r'UserBase', UserBaseViewSet)
urlpatterns = [
    url(r'docs/', schema_view)
]

urlpatterns += router.urls