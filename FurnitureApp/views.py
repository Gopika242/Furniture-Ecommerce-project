from django.shortcuts import render,redirect
from FurnitureApp.models import CategoryDb
from FurnitureApp.models import ProductDb
from WebApp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def indexPage(re):
    count1=CategoryDb.objects.count()
    ProCount=ProductDb.objects.count()
    return render(re,'index.html',{'count1':count1,'ProCount':ProCount})
def AddCategory(re):
    return render(re,'AddCategory.html')
def SaveCategory(re):
    if re.method=='POST':
        a=re.POST.get('CategoryName')
        b=re.POST.get('Description')
        c=re.FILES['CategoryImage']
        ab=CategoryDb(CategoryName=a,Description=b,CategoryImage=c)
        ab.save()
        messages.success(re,"Category Saved..!")
        return redirect('AddCategory')
def displayCategory(re):
    cd=CategoryDb.objects.all()
    return render(re,'DisplayCategory.html',{'cd':cd})

def EditCategory(re,E_id):
    data=CategoryDb.objects.get(id=E_id)
    return render(re,'EditCategory.html',{'data':data})

def UpdateCategory(re,U_id):
    if re.method=='POST':
        a3=re.POST.get('CategoryName')
        b3=re.POST.get('Description')

        try:
         c3=re.FILES['CategoryImage']
         fs=FileSystemStorage()
         file=fs.save(c3.name,c3)
        except MultiValueDictKeyError:
         file=CategoryDb.objects.get(id=U_id).CategoryImage
        CategoryDb.objects.filter(id=U_id).update(CategoryName=a3,Description=b3,CategoryImage=file)
        return redirect('displayCategory')
def DeleteCategory(re,D_id):
    bb=CategoryDb.objects.filter(id=D_id)
    bb.delete()
    return redirect('displayCategory')

def AddProduct(re):
    cat=CategoryDb.objects.all()
    return render(re,'AddProduct.html',{'cat':cat})

def SaveProduct(re):
    a4=re.POST.get('Category')
    b4=re.POST.get('ProductName')
    c4=re.POST.get('Quantity')
    d4=re.POST.get('MRP')
    e4=re.POST.get('PDescription')
    f4=re.POST.get('Country')
    g4=re.POST.get('Manufacturer')
    h4=re.FILES['ProductImage1']
    i4=re.FILES['ProductImage2']
    j4=re.FILES['ProductImage3']
    aa4=ProductDb(Category=a4,ProductName=b4,Quantity=c4,MRP=d4,PDescription=e4,Country=f4,Manufacturer=g4,ProductImage1=h4,ProductImage2=i4,ProductImage3=j4)
    aa4.save()
    messages.success(re, "Product Saved..!")
    return redirect('AddProduct')

def DisplayProduct(re):
    data=ProductDb.objects.all()
    return render(re,'DisplayProduct.html',{'data':data})

def EditProduct(re,Ep_id):
    Ed=ProductDb.objects.get(id=Ep_id)
    abb=CategoryDb.objects.all()
    return render(re,'EditProduct.html',{'Ed':Ed,'abb':abb})

def UpdateProduct(re,Up_id):
 if re.method=='POST':
    a44=re.POST.get('Category')
    b44=re.POST.get('ProductName')
    c44=re.POST.get('Quantity')
    d44=re.POST.get('MRP')
    e44=re.POST.get('PDescription')
    f44=re.POST.get('Country')
    g44=re.POST.get('Manufacturer')
    try:
     h44=re.FILES['ProductImage1']
     fs=FileSystemStorage()
     file=fs.save(h44.name,h44)
    except MultiValueDictKeyError:
     file=ProductDb.objects.get(id=Up_id).ProductImage1
    try:
     i44=re.FILES['ProductImage2']
     fs=FileSystemStorage()
     file1=fs.save(i44.name,i44)
    except MultiValueDictKeyError:
     file1=ProductDb.objects.get(id=Up_id).ProductImage2
    try:
     j44=re.FILES['ProductImage3']
     fs=FileSystemStorage()
     file2=fs.save(j44.name,j44)
    except MultiValueDictKeyError:
     file2=ProductDb.objects.get(id=Up_id).ProductImage3
    ProductDb.objects.filter(id=Up_id).update(Category=a44,ProductName=b44,Quantity=c44,MRP=d44,PDescription=e44,Country=f44,Manufacturer=g44,ProductImage1=file,ProductImage2=file1,ProductImage3=file2)
    return redirect('DisplayProduct')
def DeleteProduct(re,Dp_id):
    obj=ProductDb.objects.filter(id=Dp_id)
    obj.delete()
    messages.error(re, "Product removed..!")
    return redirect('DisplayProduct')

def Login(request):
    messages.error(request,"Logged out")
    return render(request,'AdminLogin.html')
def AdminLogin(request):
    if request.method=='POST':
        un=request.POST.get('UserName')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pswd
                messages.success(request,"Welcome..!")
                return redirect(indexPage)
            else:
                messages.error(request, "Please check your password..!")
                return redirect(Login)
        else:
            messages.warning(request, "Invalid username!")
            return redirect(Login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request, "Successfully logged out!")
    return redirect(Login)
def DisplayContact(re):
    co=ContactDb.objects.all()
    return render(re,'DisplayContact.html',{'co':co})
def DeleteContact(re,D):
    x=ContactDb.objects.filter(id=D)
    x.delete()
    return redirect('DisplayContact')