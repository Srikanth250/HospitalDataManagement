from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from hospital.models import GeneralDetails, MedicalHistory
from django.contrib.auth import logout as django_logout

# Create your views here.

def signup(request):
	if request.method == "POST":
		uname = request.POST.get('username', None)
		email = request.POST.get('email', None)
		passw = request.POST.get('password', None)
		
		if len(uname) == 0:
			return HttpResponse(f"Username can not be empty")
		elif len(email) == 0:
			return HttpResponse(f"Email can not be empty")
		elif len(passw) == 0:
			return HttpResponse(f"Password can not be empty")
		else:
			pass
			
		try:
			user = User.objects.get(username=uname)
			if user is not None:
				return HttpResponse("Please Check the Info, User might already exist.")
		except User.DoesNotExist:
			user = User.objects.create_user(uname, email, passw)
			return render(request, "signin.html")			
	return render(request, "signup.html")
	
	
def signin(request):
	if request.method == "POST":
		uname = request.POST.get('username', None)
		passw = request.POST.get('password', None)
		
		if len(uname) == 0:
			return HttpResponse(f"Username can not be empty")
		elif len(passw) == 0:
			return HttpResponse(f"Password can not be empty")
		else:
			pass
			
		user = authenticate(request, username=uname, password=passw)
		if user is not None:
			login(request, user)
			return render(request, "home.html", {"user":user})
		else:
			return HttpResponse("Verify your username and password again!")
	return render(request, "signin.html")

def homePage(request):
	return render(request, "home.html")
	
def upload(request):
	return render(request, "upload.html")

def view(request):
	return render(request, "view.html")

def validateFormElements(pfname, plname, pdob, pheight, pweight, pemail):
	if len(pfname) == 0:
		return HttpResponse(f"First Name can not be Empty")
	elif len(plname) == 0:
		return HttpResponse(f"Last Name can not be Empty")
	elif len(pdob) == 0:
		return HttpResponse(f"Date of Birth can not be Empty")
	elif len(pheight) == 0:
		return HttpResponse(f"Height can not be Empty")
	elif len(pweight) == 0:
		return HttpResponse(f"Weight can not be Empty")
	elif len(pemail) == 0:
		return HttpResponse(f"Email can not be Empty")
	else:
		pass

def general_info(request):
	if request.method == "POST":
		pgender = request.POST.get('pgender', None)
		pfname  = request.POST.get('pfname', None)
		plname  = request.POST.get('plname', None)
		pdob    = request.POST.get('pdob', None)
		pheight = request.POST.get('pheight', None)
		pweight = request.POST.get('pweight', None)
		pemail  = request.POST.get('pemail', None)
		
		validateFormElements(pfname, plname, pdob, pheight, pweight, pemail)
			
		if not pheight.isnumeric():
			return HttpResponse(f"Height accepts numbers only")
			
		if not pweight.isnumeric():
			return HttpResponse(f"Weight accepts numbers only")
		
		try:
			gen_data = GeneralDetails.objects.get(pFname=pfname)
			return HttpResponse(f" Entry already exists !")
		except GeneralDetails.DoesNotExist:
			GeneralDetails.objects.create(pGender=pgender, pFname=pfname, pLname=plname, pDOB=pdob, pHeight=pheight, pWeight=pweight, pEmail=pemail)
			return render(request, "medical_history.html", {"Pfname":pfname})
			
	return redner(request, "upload.html")
	
def med_info(request, fname):
	if request.method == "POST":
		dAllergy = request.POST.get('drug_allergy', None)
		cMed     = request.POST.get('cur_med', None)
		comment  = request.POST.get('comments', None)
		
		if len(dAllergy) == 0:
			return HttpResponse(f"Drug Allergy Can Not Be Empty")
		elif len(cMed) == 0:
			return HttpResponse(f"Current Medications Can Not Be Empty")
		elif len(comment) == 0:
			return HttpResponse(f"Doctor Comments Is Must !")
		else:
			pass
			
		disList   = []
		anemia    = request.POST.get('anemia', None)
		asthma    = request.POST.get('asthma', None)
		cancer    = request.POST.get('cancer', None)
		diabetes  = request.POST.get('diabetes', None)
		arthritis = request.POST.get('arthritis', None)
		
		if anemia == 'on':
			disList.append('anemia')
		
		if asthma == 'on':
			disList.append('asthma')

		if cancer == 'on':
			disList.append('cancer')
			
		if diabetes == 'on':
			disList.append('diabetes')
			
		if arthritis == 'on':
			disList.append('arthritis')
		
		try:
			gd = GeneralDetails.objects.get(pFname=fname)
			MedicalHistory.objects.get_or_create(patient_Id=gd, drugList=dAllergy, disList=disList, curMed=cMed, comments=comment)
			return render(request, "ack.html")
		except GeneralDetails.DoesNotExist:
			return HttpResponse(f" No matching entry found to which medical history can be linked!")
			
	return render(request, "medical_history.html", {"Pfname":fname})
	
def view_details(request):
	if request.method == "POST":
		fname = request.POST.get('username', None)
		
		if len(fname) == 0:
			return HttpResponse(f"First name can not be empty")
		else:
			pass
			
		try:
			gen_det = GeneralDetails.objects.get(pFname=fname)
		except GeneralDetails.DoesNotExist:
			return HttpResponse(f"No matching entry found for entered name !")
		
		med_det = MedicalHistory.objects.get(patient_Id=gen_det)

		return render(request, "view_details.html", {"general_data":gen_det, "medical_data":med_det})
		
def logout(request):
    django_logout(request)
    return render(request, "signin.html")