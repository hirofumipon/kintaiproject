from django.contrib import admin
from .models import Employee, Department, Position, KintaiModel, Overtimetarget

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(KintaiModel)
admin.site.register(Overtimetarget)