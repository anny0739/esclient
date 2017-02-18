from __future__ import unicode_literals
from django.db import models
# Create your models here.

class ItSearchAllGoods(models.Model):
    """IT_SEARCH_ALL_GOODS"""
    goods_seq = models.IntegerField(db_column='GOODS_SEQ', primary_key=True)
    goods_nm = models.CharField(db_column='GOODS_NM', max_length=100)
    goods_sub_nm = models.CharField(db_column='GOODS_SUB_NM', max_length=100)
    goods_sale_st = models.CharField(db_column='goods_sale_st', max_length=14)
    goods_sale_ed = models.CharField(db_column='goods_sale_ed', max_length=14)
    goods_special_price = models.IntegerField(db_column='goods_special_price', default=0)
    goods_sale_price = models.IntegerField(db_column='goods_sale_price', default=0)
    region_name = models.CharField(db_column='region_name', max_length=100)
    img_path = models.CharField(db_column='img_path', max_length=300)
    goods_region_nm = models.CharField(db_column='goods_region_nm', max_length=100)
    goods_gubun = models.CharField(db_column='goods_gubun', max_length=5)
    acc_region = models.CharField(db_column='acc_region', max_length=100)
    reg_dt = models.CharField(db_column='reg_dt', max_length=14)
    modi_dt = models.CharField(db_column='modi_dt', max_length=14)
    accommodation_keyword = models.CharField(db_column='accommodation_keyword', max_length=100)
    use_yn = models.CharField(db_column='use_yn', max_length=1)

    class Meta:
        managed = False
        db_table = 'it_search_all_goods'

    def __str__(self):
        return self.goods_nm

             