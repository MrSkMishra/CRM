from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import LeadForm,LeadModelForm
# Create your views here.

def home_page(request):
    # return HttpResponse("kya chl ra hai")
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,"leads/index.html",context)

def lead_detail(request,pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context={
        "lead":lead
    }
    return render(request,"leads/lead_detail.html",context)

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