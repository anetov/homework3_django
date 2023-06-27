from django.shortcuts import render

# Create your views here.
def login_view(request):
    # Логика обработки запроса
    return render(request, 'login.html')

def home_view(request):
    # Логика обработки запроса
    return render(request, 'home.html')