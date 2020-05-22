from django.contrib import admin
from hospital.models import GeneralDetails, MedicalHistory

# Register your models here.
myModels = [GeneralDetails, MedicalHistory]
admin.site.register(myModels)

