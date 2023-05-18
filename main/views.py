from django.shortcuts import render

# Create your views here.
def landingPageView(request):
    context = {}
    template_name = 'main/index.html'
    return render(request, template_name, context)