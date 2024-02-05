from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from .forms import regform
from .models import District, Branch, Person

# Create your views here.
def home(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            uname = request.POST['username']
            pwd = request.POST['password']
            user = auth.authenticate(username=uname,password=pwd)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')


        if 'register' in request.POST:
            return render(request, "register.html")
    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd1']
        cpwd = request.POST['pwd2']
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pwd)
                user.save();

                print("*******New User created*******")
                return redirect('firstlogin')
        else:
            messages.info(request,"Password not matching ")
            print("Password not matching")
            return redirect('register')

    return render(request,"register.html")
def firstloginkyc(request):
    if request.method == 'POST':
        return redirect('kyc')
    return render(request,"firstlogin.html")

def kyc(request):
    if request.method == 'POST':
        return redirect('kycupdate')

    return render(request,"kyc.html")
def kycupdate(request):
    return render(request, "regformkyc.html")
def branches(request):
     br = District.objects.all()
     return render(request, "header.html", {'district': br})


def displaydistrict(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'regformkyc.html')
#def displaybranch(request):

   # return render(request,'regformkyc.html')
    #print("Entered disply")
    #districts = District.objects.all()

   # context = {
   #     'dis': districts
   # }
    #return render(request,"regformkyc.html",context)

#class displaybranch(request):
     #   br_id = request.GET.get('dis_id')
   #     dis=Branch.objects.filter()
    #    return render(request, "regformkyc.html", {'dis': dis})
#class PersonListView(ListView):
 #   model = Person
  #  form_class=regform
  #  context_object_name = 'person'

#class PersonCreateView(CreateView):
 #   model = Person
    #fields = ('name', 'birthdate', 'gender', 'age','phno','email','address','district','branch','account','material')
  #  form_class = regform
   # success_url = reverse_lazy('person_changelist')

#class PersonUpdateView(UpdateView):
  #  model = Person
    #fields = ('name', 'birthdate', 'gender', 'age','phno','email','address','district','branch','account','material')
  #  form_class = regform
  #  success_url = reverse_lazy('person_changelist')
def load_cities(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('dname')
    return render(request, 'loadcities.html', {'branches': branches})

#def alldistrict(request,c_slug=None):

 #   return render(request,"regformkyc.html")

#def allbranch(request):