from django.shortcuts import render, HttpResponse, redirect
from backend_panel_app.forms import RoleDetailsForm
from backend_panel_app.models import UserRole, RoleDetails
from miscFiles.generic_functions import generate_random_string
from django.contrib.auth.hashers import make_password, check_password
from miscFiles.verify_mail import verify_link_mail


def admin_register(request):
    if request.method == "POST":
        detail_form = RoleDetailsForm(request.POST)
        role_data = UserRole.objects.get(role_name="admin")
        if detail_form.is_valid():
            form = detail_form.save(commit=False)
            form.role_id_id = role_data.role_id
            form.name = request.POST['name']
            form.mobile = request.POST['phone']
            form.email = request.POST['email']
            form.password = make_password(request.POST['password'])
            form.address = request.POST['address']
            form.gender = request.POST['gender']
            token = make_password(generate_random_string())
            token = token.replace("+", "")
            link = "127.0.0.1:8000/verify/?token={}".format(token)
            form.verify_link = token
            form.save()
            try:
                verify_link_mail(request.POST['name'], request.POST['email'], link)
            except:
                return HttpResponse("<h1>Mail not send</h1>")
            return redirect("/")
        else:
            return HttpResponse("<h1>Form not valid")
    return render(request, "registration.html")


def verify_mail(request):
    get_url = request.GET['token']
    data = RoleDetails.objects.get(verify_link=get_url)
    update = RoleDetails(id=data.id, verify_link="", is_active=1)
    update.save(update_fields=['verify_link', 'is_active'])
    return redirect("/")


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        data = RoleDetails.objects.get(email=email)
        if check_password(password, data.password):
            if data.is_active == 1:
                role = data.role_id.role_name
                if role == "admin":
                    pass
                elif role == "customer":
                    pass
                elif role == "manager":
                    pass
            else:
                return HttpResponse("Please verify your email")
        else:
            return HttpResponse("Password doesn't match")


def admin_index(request):
    return render(request, "backend_master_page.html")
