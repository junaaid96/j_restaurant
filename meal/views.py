from django.shortcuts import render

# Create your views here.
def meal(request):
    return render(request, 'meal.html')