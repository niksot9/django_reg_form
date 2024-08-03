from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def form(request):
    return render(request, 'main/form.html')

def post_form(request):
    name = request.POST.get('name', 'undefined')
    surname = request.POST.get('surname', 'undefined')
    email = request.POST.get('email', 'undefined')
    password = request.POST.get('password', 'undefined')
    confirm_password = request.POST.get('confirm_password', 'undefined')
    return HttpResponse(f"<div>Name: {name}  Surname: {surname}<div>"
                        f"<div>Email: {email}  Password: {password}<div>")

