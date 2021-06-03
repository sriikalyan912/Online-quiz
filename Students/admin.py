from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class StudentAdmin(UserAdmin):
    list_display=('StudentName','StudentRollNo','Standard')
    search_fields = ('StudentName','StudentRollNo','Standard')
    readonly_fields = ('StudentName','StudentRollNo')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

admin.site.register(Student, StudentAdmin)
