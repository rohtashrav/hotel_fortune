from django.shortcuts import render, HttpResponse, redirect
from backend_panel_app.forms import RoleDetailsForm
from backend_panel_app.models import UserRole
from miscFiles.generic_functions import generate_random_string
from django.contrib.auth.hashers import make_password
from miscFiles.verify_mail import verify_link_mail


def admin_register(request):
    if request.method == "POST":
        detail_form = RoleDetailsForm(request.POST)
        role_data = UserRole.objects.get(role_name="admin")
        if detail_form.is_valid():
            form = detail_form.save(commit=False)
            form.role_id_id = role_data.role_id
            form.name = request.POST['name']
            form.mobile = request.POST['mobile']
            form.email = request.POST['email']
            form.password = make_password(request.POST['password'])
            form.address = request.POST['address']
            form.gender = request.POST['gender']
            token = make_password(generate_random_string())
            token = token.replace("+" "")
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