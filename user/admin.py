
from django.contrib import admin
from .models import JobSeeker, Job, Admin, BaseUser


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", 'is_active')


@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name",  'is_active')
    list_filter = ("username",)
    search_fields = ("username", "email" )
    fields = (  'username','email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'date_joined', 'bio', "user_permissions")


@admin.register(JobSeeker)
class JobSeeker(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name",  'is_active')
    list_filter = ("username", )
    search_fields = ("username", "email" )
    fields = ( 'username','email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'date_joined', 'bio', "user_permissions")

@admin.register(BaseUser)
class AllUser(admin.ModelAdmin):
    list_display = ("username",  "first_name", "last_name",'is_staff', 'is_active')