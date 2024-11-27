from django.urls import path
from WebApp import views

urlpatterns=[
path('Home/',views.Home,name='Home'),
path('Products/',views.Products,name='Products'),
path('About/',views.About,name='About'),
path('Contact/',views.Contact,name='Contact'),
path('SaveContact/',views.SaveContact,name='SaveContact'),
path('ProductsFiltered/<CatName>/',views.ProductsFiltered,name='ProductsFiltered'),
path('SingleProduct/<int:Pr>/',views.SingleProduct,name='SingleProduct'),
path('Blog/',views.Blog,name='Blog'),
path('SignUp/',views.SignUp,name='SignUp'),
path('',views.SignIn,name='SignIn'),
path('SaveSignUp/',views.SaveSignUp,name='SaveSignUp'),
path('UserLogin/',views.UserLogin,name='UserLogin'),
path('UserLogout/',views.userLogout,name='UserLogout'),
path('SaveCart/',views.Save_cart,name='SaveCart'),
path('CartsPage/',views.CartsPage,name='CartsPage'),
path('CartDelete/int:<D_id>/',views.CartRemove,name='CartRemove'),
path('Checkout/',views.Checkout,name='Checkout'),
path('SaveOrder/',views.SaveOrder,name='SaveOrder'),
path('Payment/',views.Payment,name='Payment'),
]
