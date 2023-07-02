from django.shortcuts import render,redirect
from .models import ChildDetails
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
# Create your viewsa here.

@login_required(login_url='/auth/login')
def home(request):
    #count number of children/ gender
    female_count = ChildDetails.objects.filter(gender='Female').count()
    male_count = ChildDetails.objects.filter(gender='Male').count()
    total = ChildDetails.objects.all().count()
    print(female_count)
    print(male_count)
    print(total)

    context = {
        'female_count':female_count,
        'male_count':male_count,
        'total':total
    }


    return render(request, 'index.html', context)





@login_required(login_url='/auth/login')
def manageChildren(request):
    children_details = ChildDetails.objects.all()

    context = {

        'children_details':children_details,

    }



    return render(request,'child_manage.html', context)

@login_required(login_url='/auth/login')
def Add_Child(request):
    if request.method == "GET":
        return render(request,'Add_ChildForm.html')
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dateofbirth = request.POST['dateofbirth']
        status = request.POST['status']


        ChildDetails.objects.create(user=request.user,firstname=firstname,lastname=lastname,gender=gender,dateOfBirth=dateofbirth, status=status)
        messages.success(request,"The Child created successfully")
        return redirect('manage_child')
    return render(request,'Add_ChildForm.html')
    
def Child_age_range(request):
    today = date.today()
    age_ranges = {
       'under_1': ChildDetails.objects.filter(dateOfBirth__gte=today - timedelta(days=365), dateOfBirth__lt=today).count(),
       'under_2': ChildDetails.objects.filter(dateOfBirth__gte=today - timedelta(days=365 * 2), dateOfBirth__lt=today - timedelta(days=365)).count(),
       'under_3': ChildDetails.objects.filter(dateOfBirth__gte=today - timedelta(days=365 * 3), dateOfBirth__lt=today - timedelta(days=365 * 2)).count(),
       'under_4': ChildDetails.objects.filter(dateOfBirth__gte=today - timedelta(days=365 * 4), dateOfBirth__lt=today - timedelta(days=365 * 3)).count(),
       'under_5': ChildDetails.objects.filter(dateOfBirth__lt=today - timedelta(days=365 * 4)).count(),

    }

    return JsonResponse({"age_range" : age_ranges})

    
