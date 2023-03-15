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

    class Meta:
        managed = False
        db_table = 'image'


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
    april_idx = models.AutoField(primary_key=True)
    april_nansu = models.CharField(max_length=100, blank=True, null=True)
    april_memo = models.CharField(max_length=200, blank=True, null=True)
    april_pic = models.ImageField(max_length=200,blank=True, null=True)
    april_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    april_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'april_back'


class AprilFront(models.Model):
    april_idx = models.AutoField(primary_key=True)
    april_nansu = models.CharField(max_length=100, blank=True, null=True)
    april_memo = models.CharField(max_length=200, blank=True, null=True)
    april_pic = models.ImageField(max_length=200,blank=True, null=True)
    april_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    april_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'april_front'


class AugBack(models.Model):
    aug_idx = models.AutoField(primary_key=True)
    aug_nansu = models.CharField(max_length=100, blank=True, null=True)
    aug_memo = models.CharField(max_length=200, blank=True, null=True)
    aug_pic = models.ImageField(max_length=200,blank=True, null=True)
    aug_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    aug_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aug_back'


class AugFront(models.Model):
    aug_idx = models.AutoField(primary_key=True)
    aug_nansu = models.CharField(max_length=100, blank=True, null=True)
    aug_memo = models.CharField(max_length=200, blank=True, null=True)
    aug_pic = models.ImageField(max_length=200,blank=True, null=True)
    aug_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    aug_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

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
    cover_idx = models.AutoField(primary_key=True)
    cover_nansu = models.CharField(max_length=100, blank=True, null=True)
    cover_pic = models.ImageField(max_length=200,blank=True, null=True)
    cover_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    cover_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cover'


class DecBack(models.Model):
    dec_idx = models.AutoField(primary_key=True)
    dec_nansu = models.CharField(max_length=100, blank=True, null=True)
    dec_memo = models.CharField(max_length=200, blank=True, null=True)
    dec_pic = models.ImageField(max_length=200,blank=True, null=True)
    dec_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    dec_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dec_back'


class DecFront(models.Model):
    dec_idx = models.AutoField(primary_key=True)
    dec_nansu = models.CharField(max_length=100, blank=True, null=True)
    dec_memo = models.CharField(max_length=200, blank=True, null=True)
    dec_pic = models.ImageField(max_length=200,blank=True, null=True)
    dec_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    dec_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dec_front'


class FebBack(models.Model):
    feb_idx = models.AutoField(primary_key=True)
    feb_nansu = models.CharField(max_length=100, blank=True, null=True)
    feb_memo = models.CharField(max_length=200, blank=True, null=True)
    feb_pic = models.ImageField(max_length=200,blank=True, null=True)
    feb_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    feb_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'feb_back'


class FebFront(models.Model):
    feb_idx = models.AutoField(primary_key=True)
    feb_nansu = models.CharField(max_length=100, blank=True, null=True)
    feb_memo = models.CharField(max_length=200, blank=True, null=True)
    feb_pic = models.ImageField(max_length=200,blank=True, null=True)
    feb_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    feb_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'feb_front'


class JanBack(models.Model):
    jan_idx = models.AutoField(primary_key=True)
    jan_nansu = models.CharField(max_length=100, blank=True, null=True)
    jan_memo = models.CharField(max_length=200, blank=True, null=True)
    jan_pic = models.ImageField(max_length=200,blank=True, null=True)
    jan_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    jan_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jan_back'


class JanFront(models.Model):
    jan_idx = models.AutoField(primary_key=True, default=1)
    jan_nansu = models.CharField(max_length=100, blank=True, null=True)
    jan_memo = models.CharField(max_length=200, blank=True, null=True)
    jan_pic = models.ImageField(max_length=200,blank=True, null=True)
    jan_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    jan_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jan_front'


class JulyBack(models.Model):
    july_idx = models.AutoField(primary_key=True)
    july_nansu = models.CharField(max_length=100, blank=True, null=True)
    july_memo = models.CharField(max_length=200, blank=True, null=True)
    july_pic = models.ImageField(max_length=200,blank=True, null=True)
    july_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    july_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'july_back'


class JulyFront(models.Model):
    july_idx = models.AutoField(primary_key=True)
    july_nansu = models.CharField(max_length=100, blank=True, null=True)
    july_memo = models.CharField(max_length=200, blank=True, null=True)
    july_pic = models.ImageField(max_length=200,blank=True, null=True)
    july_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    july_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'july_front'


class JuneBack(models.Model):
    june_idx = models.AutoField(primary_key=True)
    june_nansu = models.CharField(max_length=100, blank=True, null=True)
    june_memo = models.CharField(max_length=200, blank=True, null=True)
    june_pic = models.ImageField(max_length=200,blank=True, null=True)
    june_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    june_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'june_back'


class JuneFront(models.Model):
    june_idx = models.AutoField(primary_key=True)
    june_nansu = models.CharField(max_length=100, blank=True, null=True)
    june_memo = models.CharField(max_length=200, blank=True, null=True)
    june_pic = models.ImageField(max_length=200,blank=True, null=True)
    june_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    june_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'june_front'


class MarBack(models.Model):
    mar_idx = models.AutoField(primary_key=True)
    mar_nansu = models.CharField(max_length=100, blank=True, null=True)
    mar_memo = models.CharField(max_length=200, blank=True, null=True)
    mar_pic = models.ImageField(max_length=200,blank=True, null=True)
    mar_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    mar_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mar_back'


class MarFront(models.Model):
    mar_idx = models.AutoField(primary_key=True)
    mar_nansu = models.CharField(max_length=100, blank=True, null=True)
    mar_memo = models.CharField(max_length=200, blank=True, null=True)
    mar_pic = models.ImageField(max_length=200,blank=True, null=True)
    mar_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    mar_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mar_front'


class MayFront(models.Model):
    may_idx = models.AutoField(primary_key=True)
    may_nansu = models.CharField(max_length=100, blank=True, null=True)
    may_memo = models.CharField(max_length=200, blank=True, null=True)
    may_pic = models.ImageField(max_length=200,blank=True, null=True)
    may_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    may_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'may_front'


class MayBack(models.Model):
    may_idx = models.AutoField(primary_key=True)
    may_nansu = models.CharField(max_length=100, blank=True, null=True)
    may_memo = models.CharField(max_length=200, blank=True, null=True)
    may_pic = models.ImageField(max_length=200,blank=True, null=True)
    may_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    may_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'may_back'


class Nansu(models.Model):
    nansu_seq = models.IntegerField(primary_key=True)
    nansu = models.CharField(max_length=100, blank=True, null=True)
    nansu_state = models.CharField(max_length=100, blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nansu'


class Notice(models.Model):
    notice = models.CharField(max_length=200, blank=True, null=True)
    notice_seq = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'notice'


class NovBack(models.Model):
    nov_idx = models.AutoField(primary_key=True)
    nov_nansu = models.CharField(max_length=100, blank=True, null=True)
    nov_memo = models.CharField(max_length=200, blank=True, null=True)
    nov_pic = models.ImageField(max_length=200,blank=True, null=True)
    nov_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    nov_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nov_back'


class NovFront(models.Model):
    nov_idx = models.AutoField(primary_key=True)
    nov_nansu = models.CharField(max_length=100, blank=True, null=True)
    nov_memo = models.CharField(max_length=200, blank=True, null=True)
    nov_pic = models.ImageField(max_length=200,blank=True, null=True)
    nov_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    nov_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nov_front'


class OctBack(models.Model):
    oct_idx = models.AutoField(primary_key=True)
    oct_nansu = models.CharField(max_length=100, blank=True, null=True)
    oct_memo = models.CharField(max_length=200, blank=True, null=True)
    oct_pic = models.ImageField(max_length=200,blank=True, null=True)
    oct_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    oct_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oct_back'


class OctFront(models.Model):
    oct_idx = models.AutoField(primary_key=True)
    oct_nansu = models.CharField(max_length=100, blank=True, null=True)
    oct_memo = models.CharField(max_length=200, blank=True, null=True)
    oct_pic = models.ImageField(max_length=200,blank=True, null=True)
    oct_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    oct_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oct_front'


class Order(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=45)
    nansu = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
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
    sep_idx = models.AutoField(primary_key=True)
    sep_nansu = models.CharField(max_length=100, blank=True, null=True)
    sep_memo = models.CharField(max_length=200, blank=True, null=True)
    sep_pic = models.ImageField(max_length=200,blank=True, null=True)
    sep_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    sep_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sep_back'


class SepFront(models.Model):
    sep_idx = models.AutoField(primary_key=True)
    sep_nansu = models.CharField(max_length=100, blank=True, null=True)
    sep_memo = models.CharField(max_length=200, blank=True, null=True)
    sep_pic = models.ImageField(max_length=200,blank=True, null=True)
    sep_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    sep_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sep_front'

class Prolog(models.Model):
    prolog_idx = models.AutoField(primary_key=True)
    prolog_nansu = models.CharField(max_length=100, blank=True, null=True)
    prolog_pic = models.ImageField(max_length=200,blank=True, null=True)
    prolog_pic2 = models.ImageField(max_length=200,blank=True, null=True)
    prolog_pic3 = models.ImageField(max_length=200,blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prolog'

# class Order(models.Model):
#     user = models.ForeignKey('users.Users', verbose_name = "사용자", on_delete = models.CASCADE)
#     product = models.ForeignKey('product.Product',verbose_name = "상품", on_delete = models.CASCADE)
#     registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
#     quantity = models.IntegerField(verbose_name="수량")

#     def __str__(self):
#         return str(self.user) + ' ' + str(self.product)
    
#     class Meta:
#         db_table = "Shoppingmall_Order"
#         verbose_name = "주문"
#         verbose_name_plural = "주문"