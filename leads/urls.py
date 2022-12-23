from django.urls import path

from leads import views

# app_name = "leads" 
urlpatterns = [
    path('',views.home_page,name="home"),
    path('<int:pk>',views.lead_detail),
    path('create/',views.lead_create,name="sendemail"),
]