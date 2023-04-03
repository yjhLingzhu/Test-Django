from django.db import models
from django.db.models.base import ModelBase
from django.db.models.fields import Field

# Create your models here.

def str_(self):
    return self.name

class DelOther(ModelBase):
    def __new__(cls, *args, **kwargs):
        # del cls.book_ptr
        # del cls.book_ptr_id
        # for key, value in args[2].items():
        #     setattr(cls, key, value)
        # print(args[2])
        return super().__new__(cls, *args, **kwargs)


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="书本名称", blank=True, null=True)
    price = models.CharField(max_length=10, verbose_name="价格", blank=True, null=True)
    addr = models.CharField(max_length=100, verbose_name="地址", blank=True, null=True)
    wx_phone_info = models.CharField(max_length=500, verbose_name="微信信息", blank=True, null=True)
    wx_openid = models.CharField(max_length=255, verbose_name="小程序id", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = "books_book"
        app_label = 'test_django'   # 数据库名/ 应用名
        # verbose_name = "书籍"
        # verbose_name_plural = verbose_name
        # ordering = ["id"]

    @classmethod
    def get_app_log_model(cls, app_name):
        class Meta:
            db_table = '{}_{}'.format(app_name, cls._meta.db_table)
            app_label = cls._meta.app_label

        attrs = {
            'Meta': Meta,
            '__module__': cls.__module__,
            '__str__': str_,
        }

        # 构建字段
        for each in cls._meta.fields:
            if isinstance(each, Field):
                attrs[each.attname] = each

        new_table = DelOther("TT", (models.Model,), attrs)
        # print(new_table.book_ptr)
        # del new_table.book_ptr
        # del new_table.book_ptr_id
        return new_table





