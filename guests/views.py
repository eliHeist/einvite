from django.shortcuts import render
from django.views.generic import ListView

from guests.models import Guest

# Create your views here.


class GuestListView(ListView):
   model = Guest
   template_name = "guests/guest-list.html"
   context_object_name = 'guests'


def addGuestView(request):
   template_name = "guests/guest-added.html"
   return render(request, template_name, {})