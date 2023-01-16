from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from .forms import LeadForm,LeadModelForm,CustomUserCreationForm
from django.views import generic   #from django.views.generic import  #TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# CRUD + L create , Retrieve, Update , Delete + List

class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render (request,"landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,"landing.html",context)

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"



def lead_detail(request,pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context={
        "lead":lead
    }
    return render(request,"leads/lead_detail.html",context)




class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:landing")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A Lead has Been Created",
            message="Go To the Site To see the new Lead",
            from_email="test@test.com",
            recipient_list= ["test2@test.com"]
        )
        return super(LeadCreateView,self).form_valid(form)

        

    


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print("Reaceiving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            print("lead has been created")
            return redirect('/')
    context  = {

        "form":form
    }
    return render(request,"leads/lead_create.html",context)



class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:landing")



def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form,
        "lead" : lead
    }
    return render(request,"leads/lead_update.html",context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:landing")



def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')




# def lead_update(request,pk):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadModelForm()
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
            
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.agent = agent
#             lead.save()
#             print("lead has been created")
#             return redirect('/')
#     context = {
#         "lead":lead,
#         "form":form
#     }
#     return render (request,"leads/lead_update.html",context)


# def lead_create(request):
# form = LeadModelForm()
# if request.method == "POST":
#     print("Reaceiving a post request")
#     form = LeadModelForm(request.POST)
#     if form.is_valid():
#         print("form is valid")
#         print(form.cleaned_data)
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         age = form.cleaned_data['age']
#         agent = form.cleaned_data['agent']
#         agent = Agent.objects.first()
#         Lead.objects.create(
#             first_name=first_name,
#             last_name = last_name,
#             age = age,
#             agent = agent

#         )
#         print("lead has been created")
#         return redirect('/')
# context  = {

#     "form":form
# }
# return render(request,"leads/lead_create.html",context)