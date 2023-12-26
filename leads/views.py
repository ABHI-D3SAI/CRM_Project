from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def lead_list(request):
    leads = Leads.objects.all()

    context = {"leads":leads}
    return render(request, "leads/lead_list.html", context)

def lead_details(request, pk):
    lead = Leads.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_details.html", context)
