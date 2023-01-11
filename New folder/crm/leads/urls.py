from django.urls import path
from .views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView,home_page

app_name = "leads"


urlpatterns = [
    path('landing',LeadListView.as_view(),name="landing"),
    path('<int:pk>',LeadDetailView.as_view(),name="detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="delete"),
    path('create/',LeadCreateView.as_view(),name="create"),
    path('',home_page,name="home"),
]