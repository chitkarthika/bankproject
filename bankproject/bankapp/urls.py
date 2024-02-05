from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('firstlogin',views.firstloginkyc,name='firstlogin'),
    path('kyc',views.kyc,name='kyc'),
    path('kycupdate',views.kycupdate,name='kycupdate'),
    path('branches',views.branches,name='branches'),
    path('displaydistrict',views.displaydistrict,name='displaydistrict'),
    #path('displaybranch',views.displaybranch,name='displaybranch'),
    #path('', views.PersonListView.as_view(), name='person_changelist'),
#    path('add/', views.PersonCreateView.as_view(), name='person_add'),
 #   path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
  #  path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    #path('<slug:c_slug>/',views.alldistrict,name='districts'),
    #path('<slug:c_slug>/<slug:branch_slug>/',views.allbranch,name='branches'),


]
