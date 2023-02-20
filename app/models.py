# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Admin(models.Model):
    admin_seq = models.IntegerField(primary_key=True)
    admin_id = models.CharField(max_length=30)
    admin_pw = models.CharField(max_length=30)
    sub_admin_id = models.CharField(max_length=30, blank=True, null=True)
    sub_admin_pw = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Calendar(models.Model):
    calendar_seq = models.IntegerField(primary_key=True)
    template_name = models.CharField(max_length=20, blank=True, null=True)
    years = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


class Nansu(models.Model):
    nansu_seq = models.IntegerField(primary_key=True)
    nansu = models.CharField(max_length=100, blank=True, null=True)
    nansu_state = models.CharField(max_length=100, blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nansu'


class Notice(models.Model):
    notice = models.CharField(max_length=200, blank=True, null=True)
    notice_seq = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'notice'


class Order(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=45)
    order_num = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    order_seq = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    zipcode = models.IntegerField()

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