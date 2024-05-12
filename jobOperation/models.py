from django.db import models
from user.models import JobSeeker, Job, Admin

class PersonalData(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=100)
    year = models.IntegerField()
    degree_name = models.CharField(max_length=100)
    positions_of_responsibility = models.TextField()
    gitHub = models.URLField()

    class Meta:
        verbose_name_plural = "Personal Data"

    def __str__(self):
        return str(self.college_name)

class JobData(models.Model):
    job_giver = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    description = models.TextField()
    stipend = models.DecimalField(max_digits=10, decimal_places=2)
    duration_of_internship = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Job Data"

    def __str__(self):
        return f"{self.company} - {self.post}"
    
class AdminContent(models.Model):
    app_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    privacy_policy = models.TextField()
    terms_and_conditions =  models.TextField()
    top_companies = models.TextField()

    class Meta:
        verbose_name_plural = "Admin Content"
