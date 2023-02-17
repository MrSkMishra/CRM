from django.urls import path

# from leads import views
# from .views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView,LandingPageView,AssignAgentView,CategoryListView
from .views import *


app_name = "leads" 


urlpatterns = [
    path('home',LeadListView.as_view(),name="landing"),
    path('',LandingPageView.as_view(),name="home"),
    path('<int:pk>',LeadDetailView.as_view(),name="detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="delete"),
    path('<int:pk>/assign-agent/',AssignAgentView.as_view(),name="assign-agent"),
    path('<int:pk>/category/',LeadCategoryUpdateView.as_view(),name="lead-category-update"),
    path('create/',LeadCreateView.as_view(),name="create"),
    path('categories/',CategoryListView.as_view(),name="category-List"),
    path('categories/<int:pk>/',CategoryDetailView.as_view(),name="category-detail"),
    # path('categories/<int:pk>/',CategoryDetailView.as_view(),name="category-detail"),

]