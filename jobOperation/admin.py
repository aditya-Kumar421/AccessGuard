from django.contrib import admin
from .models import PersonalData, JobData, AdminContent


@admin.register(PersonalData)
class PersonalData(admin.ModelAdmin):
    list_display = ('get_user_details', 'mobile_number', 'college_name', 'year')
    list_filter = ('college_name', 'year')
    search_fields = ('college_name', 'year')

    def get_user_details(self, obj):
        username = obj.job_seeker.username
        return username
    get_user_details.short_description = "User"

@admin.register(JobData)
class JobData(admin.ModelAdmin):
    list_display = ('get_user_details', 'company', 'post', 'experience',)
    list_filter = ("company", 'post',)
    search_fields = ("company",)

    def get_user_details(self, obj):
        username = obj.job_giver.username
        return username
    get_user_details.short_description = "User"

@admin.register(AdminContent)
class AdminContent(admin.ModelAdmin):
    list_display = ('get_admin_details','top_companies')
    search_fields = ('get_admin_details',)

    def get_admin_details(self, obj):
        username = obj.app_admin.username
        return username
    get_admin_details.short_description = "User"