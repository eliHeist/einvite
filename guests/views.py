from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from guests.models import Guest

# Create your views here.


class GuestListView(LoginRequiredMixin, ListView):
   model = Guest
   template_name = "guests/guest-list.html"
   context_object_name = 'guests'

   # def get_queryset(self):
   #      queryset = super().get_queryset()
   #      # Add custom filtering here
   #      return queryset.filter(is_active=True)


def addGuestView(request):
   if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        guest = Guest(name=name, email=email, phone=phone)
        guest.save()

   template_name = "guests/guest-added.html"
   return render(request, template_name, {})