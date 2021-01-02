from django.shortcuts import render,redirect
from django.contrib import messages
from  django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from .forms import SignUpForm,EditUserForm,EditAdminForm
from django.contrib.auth.models import User
# Create your views here.
def Register_view(request):
    if request.method== 'POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User created successfully.!!!!')
    else:
        fm = SignUpForm()
    return render(request,'testapp/register.html',{'form':fm})
def Login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pword=fm.cleaned_data['password']
                user=authenticate(username=uname,password=pword)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            fm = AuthenticationForm()
            return render(request,'testapp/login.html',{'form':fm})
    else:
        return redirect('profile')
def Profile_view(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            if request.user.is_superuser:
                fm=EditAdminForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserForm(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                messages.success(request,'Profile Updated')
                fm.save()
        else:
            if request.user.is_superuser:
                fm=EditAdminForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserForm(instance=request.user)
                users = None
        return render(request,'testapp/profile.html',{'name':request.user.username,'form':fm ,'users':users})
    else:
        return redirect('log_in')
def Userdetail(request,id):
    if request.user.is_authenticated:
        p=User.objects.get(id=id)
        fm=EditAdminForm(instance=p)
        return render(request,'testapp/userdetail.html',{'form':fm})
    else:
        return redirect('log_in')



def ChangePword_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Updated plze login with new password..!!')
                return redirect('profile')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'testapp/password.html',{'form':fm})
def logout_view(request):
    logout(request)
    return redirect('log_in')

