# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(max_length=200,blank=True, null=True)
    image2 = models.ImageField(max_length=200,blank=True, null=True)
    image3 = models.ImageField(max_length=200,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'

class NansuInfo(models.Model):
    info_seq = models.AutoField(primary_key=True)
    nansu_count = models.IntegerField(blank=True, null=True)
    nansu_date = models.DateTimeField(blank=True, null=True)
    template_name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nansu_info'

class Admin(models.Model):
    admin_seq = models.IntegerField(primary_key=True)
    admin_id = models.CharField(max_length=30)
    admin_pw = models.CharField(max_length=30)
    sub_admin_id = models.CharField(max_length=30, blank=True, null=True)
    sub_admin_pw = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AprilBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=10)
    april_idx = models.IntegerField(blank=True, null=True)
    april_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'april_back'


class AprilFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=9)
    april_idx = models.IntegerField(blank=True, null=True)
    april_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'april_front'


class AugBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=18)
    aug_idx = models.IntegerField(blank=True, null=True)
    aug_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'aug_back'


class AugFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=17)
    aug_idx = models.IntegerField(blank=True, null=True)
    aug_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'aug_front'



class Calendar(models.Model):
    calendar_seq = models.IntegerField(primary_key=True)
    template_name = models.CharField(max_length=20, blank=True, null=True)
    years = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar'


class Cover(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=1)
    cover_idx = models.IntegerField(blank=True, null=True)
    cover_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'cover'


class DecBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=26)
    dec_idx = models.IntegerField(blank=True, null=True)
    dec_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'dec_back'


class DecFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=25)
    dec_idx = models.IntegerField(blank=True, null=True)
    dec_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'dec_front'


class FebBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=6)
    feb_idx = models.IntegerField(blank=True, null=True)
    feb_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'feb_back'


class FebFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=5)
    feb_idx = models.IntegerField(blank=True, null=True)
    feb_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'feb_front'


class JanBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=4)
    jan_idx = models.IntegerField(blank=True, null=True)
    jan_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'jan_back'


class JanFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True, default=3)
    jan_idx = models.IntegerField(blank=True, null=True)
    jan_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'jan_front'


class JulyBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=16)
    july_idx = models.IntegerField(blank=True, null=True)
    july_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'july_back'


class JulyFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=15)
    july_idx = models.IntegerField(blank=True, null=True)
    july_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'july_front'


class JuneBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=14)
    june_idx = models.IntegerField(blank=True, null=True)
    june_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'june_back'


class JuneFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=13)
    june_idx = models.IntegerField(blank=True, null=True)
    june_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'june_front'


class MarBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=8)
    mar_idx = models.IntegerField(blank=True, null=True)
    mar_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'mar_back'


class MarFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=7)
    mar_idx = models.IntegerField(blank=True, null=True)
    mar_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'mar_front'


class MayFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=11)
    may_idx = models.IntegerField(blank=True, null=True)
    may_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'may_front'


class MayBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=12)
    may_idx = models.IntegerField(blank=True, null=True)
    may_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'may_back'


class Nansu(models.Model):
    nansu_seq = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    nansu = models.CharField(max_length=100, blank=True, null=True)
    nansu_type = models.CharField(max_length=20, blank=True, null=True)
    nansu_state = models.CharField(max_length=10)


    class Meta:
        managed = True
        db_table = 'nansu'


class Notice(models.Model):
    notice = models.CharField(max_length=200, blank=True, null=True)
    notice_idx = models.AutoField(primary_key=True)
    monthdays = models.CharField(max_length=15, blank=True, null=True)
    nansu = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notice'


class NovBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=24)
    nov_idx = models.IntegerField(blank=True, null=True)
    nov_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'nov_back'


class NovFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=23)
    nov_idx = models.IntegerField(blank=True, null=True)
    nov_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'nov_front'


class OctBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=22)
    oct_idx = models.IntegerField(blank=True, null=True)
    oct_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'oct_back'


class OctFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=21)
    oct_idx = models.IntegerField(blank=True, null=True)
    oct_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'oct_front'


class Order(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=45)
    nansu = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True) 
    order_seq = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    zipcode = models.IntegerField()
    postcode = models.CharField(max_length=20)
    detailAddress = models.CharField(max_length=30)

    ORDER_STATE_CHOICES = [
        ('미주문', '미주문'),
        ('주문신청', '주문신청'),
        ('주문완료', '주문완료'),
    ]
    orderState = models.CharField(max_length=20, choices=ORDER_STATE_CHOICES)

    class Meta:
        managed = False
        db_table = 'order'


class OrderInfo(models.Model):
    order_info_seq = models.IntegerField(primary_key=True)
    calendar_file = models.IntegerField(blank=True, null=True)
    order_state = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'order_info'


class SepBack(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=20)
    sep_idx = models.IntegerField(blank=True, null=True)
    sep_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'sep_back'


class SepFront(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=19)
    sep_idx = models.IntegerField(blank=True, null=True)
    sep_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'sep_front'

class Prolog(models.Model):
    nansu = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True,default=2)
    prolog_idx = models.IntegerField(blank=True, null=True)
    prolog_seq = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'prolog'