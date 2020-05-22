from django.db import models


# Create your models here.
class GeneralDetails(models.Model):
	pGender = models.TextField()
	pFname  = models.CharField(max_length=150, unique=True)
	pLname  = models.CharField(max_length=150)
	pDOB    = models.DateField()
	pHeight = models.IntegerField()
	pWeight = models.IntegerField()
	pEmail  = models.CharField(max_length=300)
	
	def __str__(self):
		return self.pFname
		
class MedicalHistory(models.Model):
	patient_Id = models.ForeignKey(GeneralDetails, related_name='medical', on_delete=models.CASCADE, default=None)
	drugList = models.TextField(default='NA')
	disList  = models.TextField()
	curMed   = models.TextField(default='NA')
	comments = models.TextField(default='NA')
	