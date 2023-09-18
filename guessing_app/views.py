from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ItemForm,CommentsForm
from .models import HomePageImage
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homepage(request):
    item_list=HomePageImage.objects.all()
    form= CommentsForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        return HttpResponse("<h3>thank you for comment</h3>") 
    
    context={'item_list':item_list}
    return render(request,'home.html',context)
@login_required
def CreateItem(request):
    form= ItemForm(request.POST ,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/home')
    return render(request,'item-form.html',{'form':form})