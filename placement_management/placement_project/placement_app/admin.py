from django.contrib import admin

from .models import Student, Company, Application

admin.site.register(Student)

admin.site.register(Company)

admin.site.register(Application)