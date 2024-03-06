from django.urls import path
from . import views

urlpatterns = [path("",views.index , name="index"),
               path('<int:number>/', views.calculate_price_withTax,name="calculate_price_withTax"),
               path ("taxrate/", views.view_Tax,name="view")]