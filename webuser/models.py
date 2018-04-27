from django.db import models

# Create your models here.
class UserBase(models.Model):
    sex_dic = (('man', '男'), ('woman', '女'))
    name = models.CharField(max_length=255, verbose_name='姓名')
    age = models.CharField(max_length=255, verbose_name='性别', choices=sex_dic)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name