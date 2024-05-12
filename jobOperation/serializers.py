from rest_framework import serializers
from .models import PersonalData, JobData, AdminContent


class PersonalDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='job_seeker.username', read_only=True)
    first_name = serializers.CharField(source='job_seeker.first_name', read_only=True)
    last_name = serializers.CharField(source='job_seeker.last_name', read_only=True)

    class Meta:
        model = PersonalData
        fields = ['id','username' , 'first_name', 'last_name', 'mobile_number',
                  'college_name', 'year', 'degree_name',
                  'positions_of_responsibility','gitHub', 'job_seeker']

class JobGiverSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='job_giver.email', read_only=True)
    class Meta:
        model = JobData
        fields = ['id','email', 'company', 'post', 'experience',
                   'description', 'stipend', 'duration_of_internship',
                     'skills_required','job_giver']

class AdminContentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='app_admin.username', read_only=True)
    email = serializers.CharField(source='app_admin.email', read_only=True)
    class Meta:
        model = AdminContent
        fields = ['id','username','email','privacy_policy', 'terms_and_conditions', 'top_companies', 'app_admin']