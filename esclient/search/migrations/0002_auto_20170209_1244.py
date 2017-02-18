# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_SEARCH_ALL_GOODS',
            fields=[
                ('goods_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('goods_nm', models.CharField(max_length=100)),
                ('goods_sub_nm', models.CharField(max_length=100)),
                ('goods_summary', models.CharField(max_length=200)),
                ('goods_sale_st', models.CharField(max_length=14)),
                ('goods_sale_ed', models.CharField(max_length=14)),
                ('goods_sale_price', models.IntegerField()),
                ('goods_special_price', models.IntegerField()),
                ('region_name', models.CharField(max_length=50)),
                ('img_path', models.CharField(max_length=100)),
                ('goods_region_nm', models.CharField(max_length=50)),
                ('goods_gubun', models.CharField(max_length=1)),
                ('acc_region', models.IntegerField()),
                ('reg_dt', models.CharField(max_length=14)),
                ('modi_dt', models.CharField(max_length=14)),
                ('accommodation_keyword', models.CharField(max_length=100)),
                ('use_yn', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='AllGoods',
        ),
    ]