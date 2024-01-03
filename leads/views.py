from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.decorators import login_required


class MainPageView(generic.TemplateView):
    template_name = "main_page.html"



class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CreateUser

    def get_success_url(self):
        return reverse("login")

def main_page(request):
    return render(request, "main_page.html")

@login_required(login_url='/login/')
def lead_list(request):
    leads = Leads.objects.all()

    context = {"leads":leads}
    return render(request, "leads/lead_list.html", context)

@login_required(login_url='/login/')
def lead_details(request, pk):
    lead = Leads.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_details.html", context)

@login_required(login_url='/login/')
def lead_create(request):
    form= LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            subject = 'New Lead Created'
            message =  'Checkout the website to see the new lead'#f'A new lead has been created with the name: {lead.name} and email: {lead.email}.'
            from_email = 'test@mail.com'  # Update with your email address
            recipient_list = ['user@mail.com']  # Update with the recipient's email address

            send_mail(subject, message, from_email, recipient_list)

            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }

    return render(request, "leads/lead_create.html",context)

@login_required(login_url='/login/')
def lead_update(request, pk):
    lead = Leads.objects.get(id= pk)
    form= LeadModelForm(instance = lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST,instance = lead)
        if form.is_valid():
            form.save()
        return redirect("/leads")
    context = {
        "form": form,
        "lead" : lead
    }
    return render(request, "leads/lead_update.html", context)

@login_required(login_url='/login/')
def lead_delete(request, pk):
    lead = Leads.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")






# def lead_update(request,pk):
#     lead = Leads.objects.get(id=pk)
#     form= LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name=  first_name
#             lead.last_name = last_name
#             lead.Age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead" : lead
#     }
#     return render(request, "leads/lead_update.html", context)

# def lead_create(request):
#     form= LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Leads.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 Age= age,
#                 agent=agent
#             )
#             return redirect("/leads")
#     context = {
#         "form": form
#     }

#     return render(request, "leads/lead_create.html",context)

# class LeadListView(ListView):

#     template_name = "leads/lead_list.html"
#     queryset = Leads.objects.all()
#     context_object_name = "leads"

# class LeadDetailView(DetailView):

#     template_name = "leads/lead_details.html"
#     queryset = Leads.objects.all()
#     context_object_name = "lead"

# class LeadCreateView(CreateView):

#     template_name = "leads/lead_create.html"
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return "/leads"
    

# class LeadUpdateView(UpdateView):

#     template_name = "leads/lead_update.html"
#     queryset = Leads.objects.all()
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return "/leads"


# class LeadDeleteView(DeleteView):

#     template_name = "leads/lead_delete.html"
#     queryset = Leads.objects.all()

#     def get_success_url(self):
#         return "/leads"