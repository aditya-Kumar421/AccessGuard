from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager

class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Admin(BaseUser):
    class Meta:
        verbose_name = "Admin"
        
    def __str__(self):
        return self.username

class JobSeeker(BaseUser):
    bio = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Job Seeker"

    def __str__(self):
        return self.username
    
class Job(BaseUser):
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = "Job"

    def __str__(self):
        return self.username

# Permission: Can add log entry, ID: 1
# Permission: Can change log entry, ID: 2
# Permission: Can delete log entry, ID: 3
# Permission: Can view log entry, ID: 4
# Permission: Can add group, ID: 9
# Permission: Can change group, ID: 10
# Permission: Can delete group, ID: 11
# Permission: Can view group, ID: 12
# Permission: Can add permission, ID: 5
# Permission: Can change permission, ID: 6
# Permission: Can delete permission, ID: 7
# Permission: Can view permission, ID: 8
# Permission: Can add user, ID: 13
# Permission: Can change user, ID: 14
# Permission: Can delete user, ID: 15
# Permission: Can view user, ID: 16
# Permission: Can add content type, ID: 17
# Permission: Can change content type, ID: 18
# Permission: Can delete content type, ID: 19
# Permission: Can view content type, ID: 20
# Permission: Can add session, ID: 21
# Permission: Can change session, ID: 22
# Permission: Can delete session, ID: 23
# Permission: Can view session, ID: 24
# Permission: Can add user, ID: 25
# Permission: Can change user, ID: 26
# Permission: Can delete user, ID: 27
# Permission: Can view user, ID: 28
# Permission: Can add user, ID: 29
# Permission: Can change user, ID: 30
# Permission: Can delete user, ID: 31
# Permission: Can view user, ID: 32
# Permission: Can add user, ID: 33
# Permission: Can change user, ID: 34
# Permission: Can delete user, ID: 35
# Permission: Can view user, ID: 36
