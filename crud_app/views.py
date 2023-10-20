from django.shortcuts import render,redirect
from .models import Student
# Create your views here.






def index(request):
    # getting data from database
    data= Student.objects.all()
    return render(request, 'index.html',{'data':data})

def insertData(request):
    if request.method=="POST":
        std_name = request.POST.get('name')
        std_gender = request.POST.get('gender')
        std_age = request.POST.get('age')
        std_email = request.POST.get('email')
        std_address = request.POST.get('address')
        std_phone = request.POST.get('phone')
        query = Student(std_name=std_name,
                        std_gender=std_gender,
                        std_age=std_age,
                        std_email=std_email,
                        std_address=std_address,
                        std_phone=std_phone)
        query.save()
        return redirect('index')
    return redirect(request, 'index.html')



    
def edit(request, id):
    if request.method == "POST":
        std_name = request.POST.get('name')
        std_gender = request.POST.get('gender')
        std_age = request.POST.get('age')
        std_email = request.POST.get('email')
        std_address = request.POST.get('address')
        std_phone = request.POST.get('phone')

        # Retrieve the existing student record to update
        query = Student.objects.get(id=id)
        query.std_name = std_name
        query.std_gender = std_gender
        query.std_age = std_age
        query.std_email = std_email
        query.std_address = std_address
        query.std_phone = std_phone

        # Save the updated student record
        query.save()

        return redirect('index')  # You should change 'home' to the correct URL name

    return redirect(request, 'index.html')

    

def deleteData(request,id):
    data= Student.objects.filter(id=id)
    data.delete()
    return redirect('index')
