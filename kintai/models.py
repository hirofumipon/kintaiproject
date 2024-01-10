from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Department(models.Model):
  name = models.CharField(
      verbose_name="部署名",
      max_length=50,
      )
  def __str__(self):
    return self.name
  
class Position(models.Model):
  name = models.CharField(
    verbose_name="役職名",
    max_length=50,
  )
  def __str__(self):
    return self.name

class Employee(models.Model):
  name = models.CharField(
  max_length=50,
  verbose_name ='従業員名'
  )
  
  number = models.IntegerField(
  verbose_name ='従業員番号'
  )

  department = models.ForeignKey(
    Department,
    on_delete = models.PROTECT,
    verbose_name="部署名",
    default = None,
    )
  
  position = models.ForeignKey(
    Position,
    on_delete = models.PROTECT,
    verbose_name="役職名",
    default = None,
    )
  
  def __str__(self):
    return self.name
  


class KintaiModel(models.Model):  
  employee = models.ForeignKey(
    Employee,
    on_delete = models.PROTECT,
    verbose_name ='従業員',
    default = None,
  )
  
  checkin = models.DateTimeField(
    verbose_name = '出勤時刻'
  )
  checkout = models.DateTimeField(
    verbose_name ='退勤時刻'
  )
  overtime = models.TimeField(
    verbose_name ='残業時間',
    default = '0:00:00'
  )

  hourlypaycheck = models.IntegerField(
      verbose_name="時給(残業時)",
  )
  """
  overpaycheck = models.IntegerField(
    verbose_name = '超過給料'
  )
  """
  @property
  def overpaycheck(self):
    if (self.checkout - self.checkin) >= datetime.timedelta(hours=9):
      overtime = (self.checkout - self.checkin - datetime.timedelta(hours=9)).seconds
      overpaycheck = overtime/60/60*self.hourlypaycheck
      return int(overpaycheck)
    else:
      return 0
  """
  overtimealert = models.CharField(
    verbose_name = '残業警告',
    max_length=50,
    default='問題なし',
    blank = True,
  )
  """

  @property
  def overtimealert(self):
    overtime = (self.checkout - self.checkin - datetime.timedelta(hours=9)).seconds
    overtimetarget = (Overtimetarget.objects.last().name.hour * 60 + Overtimetarget.objects.last().name.minute) * 60
    if (self.checkout - self.checkin) >= datetime.timedelta(hours=9) and overtime >= overtimetarget:
      return '残業注意'
    else:
      return ''

  reasonforabsense = models.CharField(
    max_length=50,
    verbose_name = '欠勤理由',
    blank = True,
  )


  def __str__(self):
    return self.employee.name

class Overtimetarget(models.Model):
  name = models.TimeField(
   verbose_name='目標残業時間',
   default = '0:00:00',
  )

class Budget(models.Model):
  name = models.IntegerField(
   verbose_name='人件費予算(超過分)',
  )