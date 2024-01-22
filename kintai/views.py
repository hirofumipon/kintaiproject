from django.shortcuts import render
from django.utils import timezone
from .models import KintaiModel, Overtimetarget, Budget
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime


# Create your views here.

def topfunc(request):
  return render(request, 'top.html')

def kintaitopfunc(request):
  kintaidata = KintaiModel.objects.all().order_by('-checkin','-checkout')
  overtimetarget = Overtimetarget.objects.last()
  return render(request, 'kintaiapp/index.html', {'kintaidata':kintaidata, 'overtimetarget':overtimetarget})


def allmanagementfunc(request):
  kintaidata = KintaiModel.objects.all().order_by('-checkin','-checkout')
  overtimetarget = Overtimetarget.objects.last()
  return render(request, 'kintaiapp/allmanagement.html', {'kintaidata':kintaidata, 'overtimetarget':overtimetarget})

def overtimefunc(request):
  overtimetarget = Overtimetarget.objects.last()
  filtered_data = KintaiModel.objects.filter(overtime__gte = overtimetarget.name).order_by('-checkin','-checkout')
  """
  for item in filtered_data:
    if item.overtime > overtimetarget.name:
      item.overtimealert = '残業注意'
    else:
      item.overtimealert = '問題なし'
  """
  return render(request, 'kintaiapp/overtime.html', {'filtered_data':filtered_data})



def todaycostfunc(request):
  kintai_all_data = KintaiModel.objects.all()
  '''
  kintai_all_data = KintaiModel.objects.filter(
    checkin__year = datetime.date.today().year,
    checkin__month = datetime.date.today().month,
    checkin__day = datetime.date.today().day,
  )
  '''
  budget = Budget.objects.first()

  total_overpaycheck = 0
  total_overtime = 0
  for kintai_data in kintai_all_data:
    total_overpaycheck += kintai_data.overpaycheck
    total_overtime += kintai_data.overtime.hour*60 + kintai_data.overtime.minute #時間単位を分で集計
  total_overtime = total_overtime/60 #時間を分から時に変換
  return render(request, 'kintaiapp/todaycost.html', {'total_overpaycheck' : total_overpaycheck, 'total_overtime' : total_overtime, 'budget' : budget, 'result' : budget.name - total_overpaycheck})

def detailcostfunc(request):
  return render(request, 'kintaiapp/detailcost.html')


class KintaiList(ListView):
  template_name = 'kintaiapp/edit.html'
  model = KintaiModel
  ordering = ('-checkin', '-checkout')

class KintaiDetail(DetailView):
  template_name = 'kintaiapp/detail.html'
  model = KintaiModel

class KintaiCreate(CreateView):
  template_name = 'kintaiapp/create.html'
  model = KintaiModel
  fields = '__all__'
  success_url = reverse_lazy('edit')

class KintaiUpdate(UpdateView):
  template_name = 'kintaiapp/update.html'
  model = KintaiModel
  fields = '__all__'
  success_url = reverse_lazy('edit')

class KintaiDelete(DeleteView):
  template_name = 'kintaiapp/delete.html'
  model = KintaiModel
  success_url = reverse_lazy('edit')



class OvertimetargetList(ListView):
  template_name = 'kintaiapp/overtimetarget.html'
  model = Overtimetarget

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Overtimetarget.objects.all()
    return context

class OvertimetargetUpdate(UpdateView):
  template_name = 'kintaiapp/updateovertimetarget.html'
  model = Overtimetarget
  fields = '__all__'
  success_url = reverse_lazy('overtimetarget')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Overtimetarget.objects.all()
    return context
  

class BudgetList(ListView):
  template_name = 'kintaiapp/budget.html'
  model = Budget

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Budget.objects.all()
    return context

class BudgetUpdate(UpdateView):
  template_name = 'kintaiapp/updatebudget.html'
  model = Budget
  fields = '__all__'
  success_url = reverse_lazy('budget')





