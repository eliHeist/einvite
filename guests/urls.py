from django.urls import path

from guests.views import GuestListView, addGuestView

app_name = 'guests'

urlpatterns = [
   path('', GuestListView.as_view(), name='guest-list'),
   path('confirm/', addGuestView, name='guest-confirm'),
]