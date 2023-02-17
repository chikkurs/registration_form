from django.db import models

# Create your models here.


purpose=(
    ('general','GENERAL'),
    ('fees','FEES'),
    ('leave','LEAVE'),
    ('academic','ACADEMIC')
)
CHOICES = [('MALE', 'Male'),
           ('FEMALE', 'Female')]
class Department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Branch(models.Model):
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(Department,related_name="branch",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Data(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=CHOICES)
    phone=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=100)
    purposes=models.CharField(choices=purpose,max_length=100,default='GENERAL')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name












