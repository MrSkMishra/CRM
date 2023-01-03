from django.urls import path

# from leads import views
from .views import landing_page,LeadListView,home_page,lead_detail,lead_create,lead_update,lead_delete,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView


app_name = "leads" 


urlpatterns = [
    path('landing',LeadListView.as_view(),name="landing"),
    path('',home_page,name="home"),
    path('<int:pk>',LeadDetailView.as_view(),name="detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="delete"),
    path('create/',LeadCreateView.as_view(),name="create"),
]