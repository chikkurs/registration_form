from django.db import models

# Create your models here.
choice = (
    ('mechatronics','MECHATRONICS'),
    ('mechanical','MECHANICAL'),
    ('computer','COMPUTER'),
    ('civil','CIVIL'),
    ('autoMobile','AUTOMOBILE')
)
purpose=(
    ('general','GENERAL'),
    ('fees','FEES'),
    ('leave','LEAVE'),
    ('academic','ACADEMIC')
)

class Data(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=100)
    purposes=models.CharField(choices=purpose,max_length=100,default='GENERAL')
    department=models.CharField(choices=choice,max_length=100,default='MECHANICAL')




