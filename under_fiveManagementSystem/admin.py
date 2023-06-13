from django.contrib import admin
from .models import ChildDetails

# Register your models here.
class AgeModel(admin.ModelAdmin):
    list_display=('firstname','lastname','gender','dateOfBirth','status','get_age',)

admin.site.register(ChildDetails,AgeModel)



