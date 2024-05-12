from rest_framework import serializers
from .models import  Admin, JobSeeker, Job

class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Admin
        fields = ['id', 'email', 'username', 'first_name', 'last_name','password', 'is_active', 'is_staff', 'date_joined']
        

class JobSeekerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = JobSeeker
        fields = ['id', 'email', 'username', 'first_name', 'last_name','password', 'is_active', 'is_staff', 'date_joined', 'bio']
        

class JobSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Job
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'date_joined', 'bio']
        
'''
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


from rest_framework import serializers
from .models import JobSeeker, Job, Admin

class JobSeekerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = JobSeeker
        # fields = '__all__'
        fields = ['username', 'email', 'password', 'first_name', 'last_name','bio', 'groups']

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            user = JobSeeker.objects.create(**validated_data)
            if password is not None:
                user.set_password(password)
                user.save()
            return user
    

class JobGiverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Job
        fields = ['username', 'email', 'password', 'first_name', 'last_name','bio', 'groups']
        
        def create(self, validated_data):
            password = validated_data.pop('password', None)
            user = Job.objects.create(**validated_data)
            if password is not None:
                user.set_password(password)
                user.save()
            return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        write_only_fields = ('password')

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            user = Admin.objects.create(**validated_data)
            if password is not None:
                user.set_password(password)
                user.save()
            return user
    '''