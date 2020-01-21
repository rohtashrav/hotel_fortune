from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from backend_panel_app.models import RoleDetails
from django.db.models import Q
from django.contrib.auth.hashers import check_password


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            data = RoleDetails.objects.get(email=email)
            u_password = data.password
            if check_password(password, u_password):
                pass
            else:
                return HttpResponse("Invalid Password")
        except:
            return HttpResponse("Data not found")