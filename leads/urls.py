from django.urls import path

from leads import views

app_name = "leads" 
urlpatterns = [
    path('',views.landing_page,name="landing"),
    path('home/',views.home_page,name="home"),
    path('<int:pk>',views.lead_detail,name="detail"),
    path('<int:pk>/update/',views.lead_update,name="update"),
    path('<int:pk>/delete/',views.lead_delete,name="delete"),
    path('create/',views.lead_create,name="create"),
]