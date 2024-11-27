from django.shortcuts import render,redirect
from FurnitureApp.models import ProductDb,CategoryDb
from WebApp.models import ContactDb,SignUpDb,CartDb,OrderDb
from django.contrib import messages
import razorpay

# Create your views here.
def Home(re):
    cat=CategoryDb.objects.all()
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    return render(re,'Home.html',{'cat':cat,'cart':cart})
def Products(re):
    products=ProductDb.objects.all()
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    return render(re,'Products.html',{'products':products,'cart':cart})
def About(re):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    return render(re,'About.html',{'cart':cart})
def Contact(re):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    return render(re,'contact.html',{'cart':cart})
def SaveContact(re):
    a=re.POST.get('FName')
    b=re.POST.get('LName')
    c=re.POST.get('Email')
    d=re.POST.get('Messages')
    aa=ContactDb(FName=a,LName=b,Email=c,Messages=d)
    aa.save()
    return redirect(Contact)
def ProductsFiltered(re,CatName):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    data=ProductDb.objects.filter(Category=CatName) #like id=cat_id
    return render(re,'ProductsFiltered.html',{'data':data,'cart':cart})
def SingleProduct(re,Pr):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    dat=ProductDb.objects.get(id=Pr)
    return render(re,'SingleProduct.html',{'dat':dat,'cart':cart})

def Blog(re):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    return render(re,'Blog.html',{'cart':cart})

def SignUp(re):
    return render(re,'SignUp.html')

def SaveSignUp(re):
    a1=re.POST.get('name')
    b1=re.POST.get('email')
    c1=re.POST.get('mobile')
    d1=re.POST.get('pass1')
    e1=re.POST.get('re_pass')
    obj=SignUpDb(name=a1,email=b1,mobile=c1,pass1=d1,re_pass=e1)
    if SignUpDb.objects.filter(name=a1).exists():
        messages.warning(re,"User already exits...!")
        return redirect(SignUp)
    elif SignUpDb.objects.filter(email=b1).exists():
        messages.warning(re, "User already exits...!")
        return redirect(SignUp)
    obj.save()
    return redirect(Home)

def SignIn(re):
    return render(re,'SignIn.html')

def UserLogin(request):
    if request.method=="POST":
        un=request.POST.get('name')
        pwd=request.POST.get('pass1')
        if SignUpDb.objects.filter(name=un,pass1=pwd).exists():
            request.session['name']=un
            request.session['pass1']=pwd
            messages.success(request,"You have been successfully logged in")
            return redirect(Home)
        else:
            messages.error(request, "Incorrect  Password!")
            return redirect(SignIn)
    else:
        messages.warning(request, "Check your username")
        return redirect(SignIn)

def userLogout(request):
    del request.session['name']
    del request.session['pass1']
    messages.error(request, "Logged out!")
    return redirect(Home)

def Save_cart(request):
    if request.method=="POST":
        e=request.POST.get('name')
        f=request.POST.get('ProductName')
        g=request.POST.get('Total')
        h=request.POST.get('Quantity')
        i=request.POST.get('MRP')
        obj1=CartDb(name=e,ProductName=f,Total=g,Quantity=h,MRP=i)
        obj1.save()
        messages.success(request, "Saved to cart")
        return redirect(Home)

def CartsPage(request):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    Cart=CartDb.objects.filter(name=request.session['name'])
    SubTotal=0
    ShippingAmount=0
    TotalAmount=0
    for i in Cart:
        SubTotal=SubTotal+i.Total
        if SubTotal>50000:
            ShippingAmount=100
        else:
            ShippingAmount=500
        TotalAmount=ShippingAmount+SubTotal

    return render(request,'Carts.html',{'Cart':Cart,'SubTotal':SubTotal,'ShippingAmount':ShippingAmount,'TotalAmount':TotalAmount})

def CartRemove(re,D_id):
    x=CartDb.objects.filter(id=D_id)
    x.delete()
    return redirect(CartsPage)
def Checkout(request):
    x=CartDb.objects.filter(name=re.session['name'])
    cart=x.count()
    items=CartDb.objects.filter(name=request.session['name'])
    SubTotal=0
    ShippingAmount=0
    TotalAmount=0

    for i in items:
      SubTotal=SubTotal+i.Total
      if SubTotal > 50000:
         ShippingAmount=100
      else:
         ShippingAmount=500
      TotalAmount=ShippingAmount + SubTotal
    return render(request,'Checkout.html',{'items':items,'SubTotal':SubTotal,'ShippingAmount':ShippingAmount,'TotalAmount':TotalAmount})

def SaveOrder(re):
    ab=re.POST.get('Name')
    ij=re.POST.get('Place')
    bc=re.POST.get('Email')
    cd=re.POST.get('Phone')
    ef=re.POST.get('Address')
    fg=re.POST.get('TotalAmount')
    gh=re.POST.get('Messages')
    obj1=OrderDb(Name=ab,Place=ij,Email=bc,Phone=cd,Address=ef,TotalAmount=fg,Messages=gh)
    obj1.save()
    return redirect(Payment)

def Payment(re):
    #Retrieve the data from OrderDb with the specified ID in reverse order

    customer=OrderDb.objects.order_by('-id').first()

    #Get the payment amount of the specified customer

    pay=customer.TotalAmount
    #convert the amount into paisa(Smallest currency unit)
    amount=int(pay*100)
    pay_str=str(amount)

    for i in pay_str:
        print(i)
        if re.method=="POST":
           order_currency='INR'
           client=razorpay.Client(auth=('rzp_test_XrSOnebWyMTP0h','dkXxPnKjW8WLpIREIadMAfzv'))
           payment=client.order.create({'amount':amount,'currency':order_currency})
        return render(re,'Payment.html',{'customer':customer,'pay_str':pay_str})

