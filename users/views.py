from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from .forms import RegisterForm,ProfileForm
from django.shortcuts import get_object_or_404


def register(request):
    if request.method=='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},your account is created')
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^submit")
            return redirect('/home')
    else: 
        form=RegisterForm()
        print("not submit")
    return render(request,'users/register.html',{'form':form})
@login_required
def profilepageupdate(request):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$",request.user)
    user_profile = Profile.objects.get(user=request.user)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$",user_profile,request.user.id,user_profile.age)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'users/profileupdate.html', {'form': form})

@login_required
def profilepage(request):
    profile = Profile.objects.get(user=request.user)
    print("############################################",profile)
    context={'profile':profile}
    return render(request, 'users/profile.html',context)





