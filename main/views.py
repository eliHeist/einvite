from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def landingPageView(request):
    context = {}
    template_name = 'main/index.html'
    return render(request, template_name, context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('guests:guest-list')  # Replace 'home' with the appropriate URL name for your home page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')