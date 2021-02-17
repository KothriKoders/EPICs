from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('/')
  else:
    form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('/')
    
    

    
    # for submission of the files ( to be checked)
def index(request):
      if request.method == 'POST':
            student = StudentForm(request.POST, request.FILES)
            student = StudentForm(request.POST, request.FILES)  
       if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            model_instance = student.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
       else:  
          student = StudentForm()  
           return render(request,"index.html",{'form':student})  


    
