from django.urls import path
from FurnitureApp import views
urlpatterns=[
 path('indexPage/',views.indexPage,name='indexPage'),
 path('AddCategory/',views.AddCategory,name='AddCategory'),
 path('SaveCategory/',views.SaveCategory,name='SaveCategory'),
 path('displayCategory/',views.displayCategory,name='displayCategory'),
 path('EditCategory/<int:E_id>/',views.EditCategory,name='EditCategory'),
 path('UpdateCategory/<int:U_id>/', views.UpdateCategory, name='UpdateCategory'),
 path('DeleteCategory/<int:D_id>/', views.DeleteCategory, name='DeleteCategory'),


 path('AddProduct/',views.AddProduct,name='AddProduct'),
 path('SaveProduct/', views.SaveProduct, name='SaveProduct'),
 path('DisplayProduct/', views.DisplayProduct, name='DisplayProduct'),
 path('EditProduct/<int:Ep_id>/', views.EditProduct, name='EditProduct'),
 path('UpdateProduct/<int:Up_id>/', views.UpdateProduct, name='UpdateProduct'),
 path('DeleteProduct/<int:Dp_id>/', views.DeleteProduct, name='DeleteProduct'),


 path('LoginPage/', views.Login, name='LoginPage'),
 path('AdminLogin/', views.AdminLogin, name='AdminLogin'),
 path('admin_logout/',views.admin_logout,name='admin_logout'),
 path('DisplayContact/',views.DisplayContact,name='DisplayContact'),
 path('DeleteContact/<int:D>/', views.DeleteContact, name='DeleteContact')

]