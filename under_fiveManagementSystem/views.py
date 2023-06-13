from django.shortcuts import render,redirect
from .models import ChildDetails
from django.contrib import messages
from django.db.models import Count
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
        messages.success(request,"The Child created succefully")
        return redirect('manage_child')
    return render(request,'Add_ChildForm.html')
    

