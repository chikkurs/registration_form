from django.contrib import admin

# Register your models here.
from .models import Data,Department,Branch

admin.site.register(Data)
admin.site.register(Department)
admin.site.register(Branch)

