from django.contrib import admin
from.models import Contact,Staff,Departments

# Register your models here.
class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)


admin.site.register(Staff)
admin.site.register(Departments)