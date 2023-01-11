from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from .forms import LeadForm,LeadModelForm,CustomUsercreation
from django.views import generic


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUsercreation

    def get_success_url(self):
        return reverse ("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListView(generic.ListView):
    template_name = "leads/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:landing")

    def form_valid(self, form):
        send_mail (
            subject= "A Lead has Been Created",
            message="Go To the Site To see the new Lead",
            from_email="mishrasonu9211@gmail.com",
            recipient_list= ["mishrasonu9211@gmail.com"]
        )
        return super(LeadCreateView,self).form_valid(form)

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm


    def get_success_url(self):
        return reverse ("leads:landing")


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()


    def get_success_url(self):
        return reverse("leads:landing")

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,"landing.html",context)